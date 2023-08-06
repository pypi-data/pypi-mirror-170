const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { s as stringCompare } from './compare-dev.js';
import { d as debounce } from './stop_propagation-dev.js';
import { ab as createCollection, j as computeStateName } from './auth-dev.js';

const createAreaRegistryEntry=(hass,values)=>hass.callWS({type:"config/area_registry/create",...values});const fetchAreaRegistry=conn=>conn.sendMessagePromise({type:"config/area_registry/list"}).then(areas=>areas.sort((ent1,ent2)=>stringCompare(ent1.name,ent2.name)));const subscribeAreaRegistryUpdates=(conn,store)=>conn.subscribeEvents(debounce(()=>fetchAreaRegistry(conn).then(areas=>store.setState(areas,true)),500,true),"area_registry_updated");const subscribeAreaRegistry=(conn,onChange)=>createCollection("_areaRegistry",fetchAreaRegistry,subscribeAreaRegistryUpdates,conn,onChange);

const fallbackDeviceName=(hass,entities)=>{for(const entity of entities||[]){const entityId=typeof entity==="string"?entity:entity.entity_id;const stateObj=hass.states[entityId];if(stateObj){return computeStateName(stateObj);}}return undefined;};const computeDeviceName=(device,hass,entities)=>device.name_by_user||device.name||entities&&fallbackDeviceName(hass,entities)||hass.localize("ui.panel.config.devices.unnamed_device","type",hass.localize(`ui.panel.config.devices.type.${device.entry_type||"device"}`));const updateDeviceRegistryEntry=(hass,deviceId,updates)=>hass.callWS({type:"config/device_registry/update",device_id:deviceId,...updates});const fetchDeviceRegistry=conn=>conn.sendMessagePromise({type:"config/device_registry/list"});const subscribeDeviceRegistryUpdates=(conn,store)=>conn.subscribeEvents(debounce(()=>fetchDeviceRegistry(conn).then(devices=>store.setState(devices,true)),500,true),"device_registry_updated");const subscribeDeviceRegistry=(conn,onChange)=>createCollection("_dr",fetchDeviceRegistry,subscribeDeviceRegistryUpdates,conn,onChange);

export { subscribeAreaRegistry as a, computeDeviceName as b, createAreaRegistryEntry as c, subscribeDeviceRegistry as s, updateDeviceRegistryEntry as u };
