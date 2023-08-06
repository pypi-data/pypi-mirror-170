const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { s as subscribeOne } from './subscribe-one-dev.js';
import { g as getConfigEntries } from './config_entries-dev.js';
import { aR as getCollection, ac as subscribeEntityRegistry } from './auth-dev.js';
import { ad as startOfYesterday, ae as fetchStatistics } from './ha-more-info-dialog-dev.js';
import { e as endOfDay, s as startOfDay, c as addHours, d as differenceInDays } from './index-dev3.js';

/**
 * @name endOfToday
 * @category Day Helpers
 * @summary Return the end of today.
 * @pure false
 *
 * @description
 * Return the end of today.
 *
 * > ⚠️ Please note that this function is not present in the FP submodule as
 * > it uses `Date.now()` internally hence impure and can't be safely curried.
 *
 * @returns {Date} the end of today
 *
 * @example
 * // If today is 6 October 2014:
 * const result = endOfToday()
 * //=> Mon Oct 6 2014 23:59:59.999
 */function endOfToday(){return endOfDay(Date.now());}

/**
 * @name endOfYesterday
 * @category Day Helpers
 * @summary Return the end of yesterday.
 * @pure false
 *
 * @description
 * Return the end of yesterday.
 *
 * > ⚠️ Please note that this function is not present in the FP submodule as
 * > it uses `new Date()` internally hence impure and can't be safely curried.
 *
 * @returns {Date} the end of yesterday
 *
 * @example
 * // If today is 6 October 2014:
 * const result = endOfYesterday()
 * //=> Sun Oct 5 2014 23:59:59.999
 */function endOfYesterday(){var now=new Date();var year=now.getFullYear();var month=now.getMonth();var day=now.getDate();var date=new Date(0);date.setFullYear(year,month,day-1);date.setHours(23,59,59,999);return date;}

/**
 * @name startOfToday
 * @category Day Helpers
 * @summary Return the start of today.
 * @pure false
 *
 * @description
 * Return the start of today.
 *
 * > ⚠️ Please note that this function is not present in the FP submodule as
 * > it uses `Date.now()` internally hence impure and can't be safely curried.
 *
 * @returns {Date} the start of today
 *
 * @example
 * // If today is 6 October 2014:
 * const result = startOfToday()
 * //=> Mon Oct 6 2014 00:00:00
 */function startOfToday(){return startOfDay(Date.now());}

const groupBy=(list,keySelector)=>{const result={};for(const item of list){const key=keySelector(item);if(key in result){result[key].push(item);}else {result[key]=[item];}}return result;};

const energyCollectionKeys=[];const getEnergyInfo=hass=>hass.callWS({type:"energy/info"});const getEnergyPreferences=hass=>hass.callWS({type:"energy/get_prefs"});const getFossilEnergyConsumption=async(hass,startTime,energy_statistic_ids,co2_statistic_id,endTime,period="hour")=>hass.callWS({type:"energy/fossil_energy_consumption",start_time:startTime.toISOString(),end_time:endTime===null||endTime===void 0?void 0:endTime.toISOString(),energy_statistic_ids,co2_statistic_id,period});const energySourcesByType=prefs=>groupBy(prefs.energy_sources,item=>item.type);const getEnergyData=async(hass,prefs,start,end)=>{const[configEntries,entityRegistryEntries,info]=await Promise.all([getConfigEntries(hass),subscribeOne(hass.connection,subscribeEntityRegistry),getEnergyInfo(hass)]);const co2SignalConfigEntry=configEntries.find(entry=>entry.domain==="co2signal");let co2SignalEntity;if(co2SignalConfigEntry){for(const entry of entityRegistryEntries){if(entry.config_entry_id!==co2SignalConfigEntry.entry_id){continue;}// The integration offers 2 entities. We want the % one.
const co2State=hass.states[entry.entity_id];if(!co2State||co2State.attributes.unit_of_measurement!=="%"){continue;}co2SignalEntity=co2State.entity_id;break;}}const consumptionStatIDs=[];const statIDs=[];for(const source of prefs.energy_sources){if(source.type==="solar"){statIDs.push(source.stat_energy_from);continue;}if(source.type==="gas"){statIDs.push(source.stat_energy_from);if(source.stat_cost){statIDs.push(source.stat_cost);}const costStatId=info.cost_sensors[source.stat_energy_from];if(costStatId){statIDs.push(costStatId);}continue;}if(source.type==="battery"){statIDs.push(source.stat_energy_from);statIDs.push(source.stat_energy_to);continue;}// grid source
for(const flowFrom of source.flow_from){consumptionStatIDs.push(flowFrom.stat_energy_from);statIDs.push(flowFrom.stat_energy_from);if(flowFrom.stat_cost){statIDs.push(flowFrom.stat_cost);}const costStatId=info.cost_sensors[flowFrom.stat_energy_from];if(costStatId){statIDs.push(costStatId);}}for(const flowTo of source.flow_to){statIDs.push(flowTo.stat_energy_to);if(flowTo.stat_compensation){statIDs.push(flowTo.stat_compensation);}const costStatId=info.cost_sensors[flowTo.stat_energy_to];if(costStatId){statIDs.push(costStatId);}}}const dayDifference=differenceInDays(end||new Date(),start);// Subtract 1 hour from start to get starting point data
const startMinHour=addHours(start,-1);const stats=await fetchStatistics(hass,startMinHour,end,statIDs,dayDifference>35?"month":dayDifference>2?"day":"hour");let fossilEnergyConsumption;if(co2SignalEntity!==undefined){fossilEnergyConsumption=await getFossilEnergyConsumption(hass,start,consumptionStatIDs,co2SignalEntity,end,dayDifference>35?"month":dayDifference>2?"day":"hour");}Object.values(stats).forEach(stat=>{// if the start of the first value is after the requested period, we have the first data point, and should add a zero point
if(stat.length&&new Date(stat[0].start)>startMinHour){stat.unshift({...stat[0],start:startMinHour.toISOString(),end:startMinHour.toISOString(),sum:0,state:0});}});const data={start,end,info,prefs,stats,co2SignalConfigEntry,co2SignalEntity,fossilEnergyConsumption};return data;};const getEnergyDataCollection=(hass,options={})=>{let key="_energy";if(options.key){if(!options.key.startsWith("energy_")){throw new Error("Key need to start with energy_");}key=`_${options.key}`;}if(hass.connection[key]){return hass.connection[key];}energyCollectionKeys.push(options.key);const collection=getCollection(hass.connection,key,async()=>{if(!collection.prefs){// This will raise if not found.
// Detect by checking `e.code === "not_found"
collection.prefs=await getEnergyPreferences(hass);}if(collection._refreshTimeout){clearTimeout(collection._refreshTimeout);}if(collection._active&&(!collection.end||collection.end>new Date())){// The stats are created every hour
// Schedule a refresh for 20 minutes past the hour
// If the end is larger than the current time.
const nextFetch=new Date();if(nextFetch.getMinutes()>=20){nextFetch.setHours(nextFetch.getHours()+1);}nextFetch.setMinutes(20,0,0);collection._refreshTimeout=window.setTimeout(()=>collection.refresh(),nextFetch.getTime()-Date.now());}return getEnergyData(hass,collection.prefs,collection.start,collection.end);});const origSubscribe=collection.subscribe;collection.subscribe=subscriber=>{const unsub=origSubscribe(subscriber);collection._active++;return ()=>{collection._active--;if(collection._active<1){clearTimeout(collection._refreshTimeout);collection._refreshTimeout=undefined;}unsub();};};collection._active=0;collection.prefs=options.prefs;const now=new Date();// Set start to start of today if we have data for today, otherwise yesterday
collection.start=now.getHours()>0?startOfToday():startOfYesterday();collection.end=now.getHours()>0?endOfToday():endOfYesterday();const scheduleUpdatePeriod=()=>{collection._updatePeriodTimeout=window.setTimeout(()=>{collection.start=startOfToday();collection.end=endOfToday();scheduleUpdatePeriod();},addHours(endOfToday(),1).getTime()-Date.now()// Switch to next day an hour after the day changed
);};scheduleUpdatePeriod();collection.clearPrefs=()=>{collection.prefs=undefined;};collection.setPeriod=(newStart,newEnd)=>{var _collection$end;collection.start=newStart;collection.end=newEnd;if(collection.start.getTime()===startOfToday().getTime()&&((_collection$end=collection.end)===null||_collection$end===void 0?void 0:_collection$end.getTime())===endOfToday().getTime()&&!collection._updatePeriodTimeout){scheduleUpdatePeriod();}else if(collection._updatePeriodTimeout){clearTimeout(collection._updatePeriodTimeout);collection._updatePeriodTimeout=undefined;}};return collection;};const getEnergySolarForecasts=hass=>hass.callWS({type:"energy/solar_forecast"});const getEnergyGasUnit=(hass,prefs)=>{for(const source of prefs.energy_sources){if(source.type!=="gas"){continue;}const entity=hass.states[source.stat_energy_from];if(entity!==null&&entity!==void 0&&entity.attributes.unit_of_measurement){// Wh is normalized to kWh by stats generation
return entity.attributes.unit_of_measurement==="Wh"?"kWh":entity.attributes.unit_of_measurement;}}return undefined;};

export { endOfToday as a, getEnergyGasUnit as b, getEnergySolarForecasts as c, energySourcesByType as e, getEnergyDataCollection as g, startOfToday as s };
