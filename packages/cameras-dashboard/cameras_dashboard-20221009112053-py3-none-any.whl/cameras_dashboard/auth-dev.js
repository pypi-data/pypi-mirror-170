const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { d as debounce } from './stop_propagation-dev.js';
import { aF as mdiBookmark, M as mdiAlert, aG as mdiAirFilter, aH as mdiRobot, aI as mdiCalendar, aJ as mdiVideo, aK as mdiThermostat, au as mdiCog, aL as mdiTextToSpeech, aM as mdiCounter, am as mdiFan, aN as mdiGoogleAssistant, aO as mdiGoogleCirclesCommunities, aP as mdiHomeAssistant, aQ as mdiHomeAutomation, aR as mdiImageFilterFrames, aS as mdiGestureTapButton, aT as mdiCalendarClock, aU as mdiRayVertex, aV as mdiFormatListBulleted, aW as mdiFormTextbox, aX as mdiLightbulb, aY as mdiMailbox, aZ as mdiCommentAlert, a_ as mdiBell, a$ as mdiAccount, b0 as mdiFlower, b1 as mdiAppleSafari, b2 as mdiRemote, b3 as mdiPalette, b4 as mdiScriptText, b5 as mdiEye, b6 as mdiBullhorn, b7 as mdiWhiteBalanceSunny, b8 as mdiTimerOutline, b9 as mdiCloudUpload, ba as mdiRobotVacuum, bb as mdiThermometer, bc as mdiWeatherCloudy, bd as mdiMapMarkerRadius, h as mdiFlash, be as mdiMoleculeCo2, bf as mdiMoleculeCo, bg as mdiCurrentAc, bh as mdiLightningBolt, bi as mdiSineWave, bj as mdiGasCylinder, an as mdiWaterPercent, bk as mdiBrightness5, bl as mdiCash, bm as mdiMolecule, bn as mdiAngleAcute, aq as mdiGauge, bo as mdiWifi, bp as mdiClock, b as memoizeOne, f as fireEvent, U as __extends, V as __assign, ay as MDCFoundation, ah as __decorate, d as e$1, aB as observer, bq as ariaProperty, G as i$1, R as e$2, t, K as e$3, az as BaseElement, T as RippleHandlers, aA as addHasRemoveClass, $, Q as l$1, r as r$1, _ as _decorate, j as _get, k as _getPrototypeOf, n as n$2, br as Polymer, q as html, E as dom, bs as mdiShield, bt as mdiShieldOff, bu as mdiBellRing, bv as mdiShieldOutline, bw as mdiSecurity, bx as mdiShieldMoon, by as mdiShieldHome, bz as mdiShieldAirplane, bA as mdiShieldLock, bB as mdiRadioboxBlank, bC as mdiCheckboxMarkedCircle, bD as mdiWindowClosed, bE as mdiWindowOpen, bF as mdiCropPortrait, bG as mdiVibrate, bH as mdiPackage, bI as mdiPackageUp, bJ as mdiMusicNoteOff, bK as mdiMusicNote, A as mdiStop, a5 as mdiPlay, bL as mdiHomeOutline, bM as mdiHome, bN as mdiPowerPlugOff, bO as mdiPowerPlug, bP as mdiSquare, bQ as mdiSquareOutline, bR as mdiMotionSensorOff, bS as mdiMotionSensor, bT as mdiWaterOff, bU as mdiWater, bV as mdiLock, bW as mdiLockOpen, bX as mdiBrightness7, ak as mdiFire, bY as mdiCheckCircle, bZ as mdiSmoke, b_ as mdiAlertCircle, b$ as mdiGarage, c0 as mdiGarageOpen, c1 as mdiDoorClosed, c2 as mdiDoorOpen, c3 as mdiCloseNetworkOutline, c4 as mdiCheckNetworkOutline, al as mdiSnowflake, c5 as mdiBattery, c6 as mdiBatteryCharging, c7 as mdiBatteryOutline, c8 as mdiArrowUp, c9 as mdiArrowExpandHorizontal, ca as mdiArrowDown, cb as mdiArrowCollapseHorizontal, cc as mdiArrowDownBox, cd as mdiArrowUpBox, ce as mdiBlindsOpen, cf as mdiBlinds, cg as mdiCurtains, ch as mdiCurtainsClosed, ci as mdiArrowSplitVertical, cj as mdiWindowShutterOpen, ck as mdiWindowShutter, cl as mdiCircle, cm as mdiCircleSlice8, cn as mdiGateOpen, co as mdiGate, cp as mdiGateArrowRight, cq as mdiBatteryAlert, cr as mdiBatteryUnknown, cs as mdiBatteryChargingOutline, ct as mdiBatteryAlertVariantOutline, cu as mdiBattery10, cv as mdiBattery20, cw as mdiBattery30, cx as mdiBattery40, cy as mdiBattery50, cz as mdiBattery60, cA as mdiBattery70, cB as mdiBattery80, cC as mdiBattery90, cD as mdiBatteryCharging10, cE as mdiBatteryCharging20, cF as mdiBatteryCharging30, cG as mdiBatteryCharging40, cH as mdiBatteryCharging50, cI as mdiBatteryCharging60, cJ as mdiBatteryCharging70, cK as mdiBatteryCharging80, cL as mdiBatteryCharging90, cM as mdiWeatherNight, cN as mdiZWave, cO as mdiTimerSand, cP as mdiSleep, cQ as mdiEmoticonDead, cR as mdiToggleSwitch, cS as mdiToggleSwitchOff, cT as mdiCastConnected, cU as mdiCast, cV as mdiLockClock, cW as mdiLockAlert, cX as mdiCheckCircleOutline, cY as mdiCloseCircleOutline, cZ as mdiAirHumidifierOff, c_ as mdiAirHumidifier, c$ as mdiLanConnect, d0 as mdiLanDisconnect, d1 as mdiBluetoothConnect, d2 as mdiBluetooth, d3 as mdiAccountArrowRight, d4 as mdiRestart, c as s$1, I as i$2, d5 as mdiAlbum, d6 as mdiApplication, d7 as mdiAccountMusic, d8 as mdiTelevisionClassic, d9 as mdiAccountMusicOutline, da as mdiFolder, db as mdiGamepadVariant, dc as mdiDramaMasks, dd as mdiImage, de as mdiMovie, df as mdiMusic, dg as mdiPlaylistMusic, dh as mdiPodcast, di as mdiFileMusic, dj as mdiWeb, a8 as mdiPower, a4 as mdiSkipPrevious, ad as mdiPlayPause, a6 as mdiPause, a7 as mdiSkipNext, i as i$3, dk as r$2, J as t$1, e as e$4, O as b, dl as t$2 } from './main-dev.js';

/** Return if a component is loaded. */const isComponentLoaded=(hass,component)=>hass&&hass.config.components.includes(component);

// Arrays with values should be alphabetically sorted if order doesn't matter.
// Each constant should have a description what it is supposed to be used for.
/** Icon to use when no icon specified for domain. */const DEFAULT_DOMAIN_ICON=mdiBookmark;/** Icons for each domain */const FIXED_DOMAIN_ICONS={alert:mdiAlert,air_quality:mdiAirFilter,automation:mdiRobot,calendar:mdiCalendar,camera:mdiVideo,climate:mdiThermostat,configurator:mdiCog,conversation:mdiTextToSpeech,counter:mdiCounter,fan:mdiFan,google_assistant:mdiGoogleAssistant,group:mdiGoogleCirclesCommunities,homeassistant:mdiHomeAssistant,homekit:mdiHomeAutomation,image_processing:mdiImageFilterFrames,input_button:mdiGestureTapButton,input_datetime:mdiCalendarClock,input_number:mdiRayVertex,input_select:mdiFormatListBulleted,input_text:mdiFormTextbox,light:mdiLightbulb,mailbox:mdiMailbox,notify:mdiCommentAlert,number:mdiRayVertex,persistent_notification:mdiBell,person:mdiAccount,plant:mdiFlower,proximity:mdiAppleSafari,remote:mdiRemote,scene:mdiPalette,script:mdiScriptText,select:mdiFormatListBulleted,sensor:mdiEye,siren:mdiBullhorn,simple_alarm:mdiBell,sun:mdiWhiteBalanceSunny,timer:mdiTimerOutline,updater:mdiCloudUpload,vacuum:mdiRobotVacuum,water_heater:mdiThermometer,weather:mdiWeatherCloudy,zone:mdiMapMarkerRadius};const FIXED_DEVICE_CLASS_ICONS={apparent_power:mdiFlash,aqi:mdiAirFilter,// battery: mdiBattery, => not included by design since `sensorIcon()` will dynamically determine the icon
carbon_dioxide:mdiMoleculeCo2,carbon_monoxide:mdiMoleculeCo,current:mdiCurrentAc,date:mdiCalendar,energy:mdiLightningBolt,frequency:mdiSineWave,gas:mdiGasCylinder,humidity:mdiWaterPercent,illuminance:mdiBrightness5,monetary:mdiCash,nitrogen_dioxide:mdiMolecule,nitrogen_monoxide:mdiMolecule,nitrous_oxide:mdiMolecule,ozone:mdiMolecule,pm1:mdiMolecule,pm10:mdiMolecule,pm25:mdiMolecule,power:mdiFlash,power_factor:mdiAngleAcute,pressure:mdiGauge,reactive_power:mdiFlash,signal_strength:mdiWifi,sulphur_dioxide:mdiMolecule,temperature:mdiThermometer,timestamp:mdiClock,volatile_organic_compounds:mdiMolecule,voltage:mdiSineWave};/** Domains that have a state card. */const DOMAINS_WITH_CARD=["button","climate","cover","configurator","input_button","input_select","input_number","input_text","lock","media_player","number","scene","script","select","timer","vacuum","water_heater"];/** Domains with separate more info dialog. */const DOMAINS_WITH_MORE_INFO=["alarm_control_panel","automation","camera","climate","configurator","counter","cover","fan","group","humidifier","input_datetime","light","lock","media_player","person","remote","script","scene","sun","timer","vacuum","water_heater","weather"];/** Domains that do not show the default more info dialog content (e.g. the attribute section)
 *  and do not have a separate more info (so not in DOMAINS_WITH_MORE_INFO). */const DOMAINS_HIDE_DEFAULT_MORE_INFO=["input_number","input_select","input_text","number","scene","select"];/** Domains that render an input element instead of a text value when displayed in a row.
 *  Those rows should then not show a cursor pointer when hovered (which would normally
 *  be the default) unless the element itself enforces it (e.g. a button). Also those elements
 *  should not act as a click target to open the more info dialog (the row name and state icon
 *  still do of course) as the click should instead e.g. activate the input field  or toggle
 *  the button that this row shows.
 */const DOMAINS_INPUT_ROW=["automation","button","cover","fan","group","humidifier","input_boolean","input_button","input_datetime","input_number","input_select","input_text","light","lock","media_player","number","scene","script","select","switch","vacuum"];/** Domains that should have the history hidden in the more info dialog. */const DOMAINS_MORE_INFO_NO_HISTORY=["camera","configurator"];/** States that we consider "off". */const STATES_OFF=["closed","locked","off"];/** Binary States */const BINARY_STATE_ON="on";const BINARY_STATE_OFF="off";/** Domains where we allow toggle in Lovelace. */const DOMAINS_TOGGLE=new Set(["fan","input_boolean","light","switch","script","group","automation","humidifier"]);/** Domains that have a dynamic entity image / picture. */const DOMAINS_WITH_DYNAMIC_PICTURE=new Set(["camera","media_player"]);/** Temperature units. */const UNIT_C="°C";const UNIT_F="°F";

const computeDomain=entityId=>entityId.substr(0,entityId.indexOf("."));

/** Compute the object ID of a state. */const computeObjectId=entityId=>entityId.substr(entityId.indexOf(".")+1);

const computeStateName=stateObj=>stateObj.attributes.friendly_name===undefined?computeObjectId(stateObj.entity_id).replace(/_/g," "):stateObj.attributes.friendly_name||"";

const createStore=state=>{let listeners=[];function unsubscribe(listener){let out=[];for(let i=0;i<listeners.length;i++){if(listeners[i]===listener){listener=null;}else {out.push(listeners[i]);}}listeners=out;}function setState(update,overwrite){state=overwrite?update:Object.assign(Object.assign({},state),update);let currentListeners=listeners;for(let i=0;i<currentListeners.length;i++){currentListeners[i](state);}}/**
     * An observable state container, returned from {@link createStore}
     * @name store
     */return {get state(){return state;},/**
         * Create a bound copy of the given action function.
         * The bound returned function invokes action() and persists the result back to the store.
         * If the return value of `action` is a Promise, the resolved value will be used as state.
         * @param {Function} action	An action of the form `action(state, ...args) -> stateUpdate`
         * @returns {Function} boundAction()
         */action(action){function apply(result){setState(result,false);}// Note: perf tests verifying this implementation: https://esbench.com/bench/5a295e6299634800a0349500
return function(){let args=[state];for(let i=0;i<arguments.length;i++)args.push(arguments[i]);// @ts-ignore
let ret=action.apply(this,args);if(ret!=null){return ret instanceof Promise?ret.then(apply):apply(ret);}};},/**
         * Apply a partial state object to the current state, invoking registered listeners.
         * @param {Object} update				An object with properties to be merged into state
         * @param {Boolean} [overwrite=false]	If `true`, update will replace state instead of being merged into it
         */setState,/**
         * Register a listener function to be called whenever state is changed. Returns an `unsubscribe()` function.
         * @param {Function} listener	A function to call when state changes. Gets passed the new state.
         * @returns {Function} unsubscribe()
         */subscribe(listener){listeners.push(listener);return ()=>{unsubscribe(listener);};}// /**
//  * Remove a previously-registered listener function.
//  * @param {Function} listener	The callback previously passed to `subscribe()` that should be removed.
//  * @function
//  */
// unsubscribe,
};};

const getCollection=(conn,key,fetchCollection,subscribeUpdates)=>{if(conn[key]){return conn[key];}let active=0;let unsubProm;let store=createStore();const refresh=()=>fetchCollection(conn).then(state=>store.setState(state,true));const refreshSwallow=()=>refresh().catch(err=>{// Swallow errors if socket is connecting, closing or closed.
// We will automatically call refresh again when we re-establish the connection.
if(conn.connected){throw err;}});conn[key]={get state(){return store.state;},refresh,subscribe(subscriber){active++;// If this was the first subscriber, attach collection
if(active===1){if(subscribeUpdates){unsubProm=subscribeUpdates(conn,store);}// Fetch when connection re-established.
conn.addEventListener("ready",refreshSwallow);refreshSwallow();}const unsub=store.subscribe(subscriber);if(store.state!==undefined){// Don't call it right away so that caller has time
// to initialize all the things.
setTimeout(()=>subscriber(store.state),0);}return ()=>{unsub();active--;if(!active){// Unsubscribe from changes
if(unsubProm)unsubProm.then(unsub=>{unsub();});conn.removeEventListener("ready",refresh);}};}};return conn[key];};// Legacy name. It gets a collection and subscribes.
const createCollection=(key,fetchCollection,subscribeUpdates,conn,onChange)=>getCollection(conn,key,fetchCollection,subscribeUpdates).subscribe(onChange);

const getExtendedEntityRegistryEntry=(hass,entityId)=>hass.callWS({type:"config/entity_registry/get",entity_id:entityId});const updateEntityRegistryEntry=(hass,entityId,updates)=>hass.callWS({type:"config/entity_registry/update",entity_id:entityId,...updates});const removeEntityRegistryEntry=(hass,entityId)=>hass.callWS({type:"config/entity_registry/remove",entity_id:entityId});const fetchEntityRegistry=conn=>conn.sendMessagePromise({type:"config/entity_registry/list"});const subscribeEntityRegistryUpdates=(conn,store)=>conn.subscribeEvents(debounce(()=>fetchEntityRegistry(conn).then(entities=>store.setState(entities,true)),500,true),"entity_registry_updated");const subscribeEntityRegistry=(conn,onChange)=>createCollection("_entityRegistry",fetchEntityRegistry,subscribeEntityRegistryUpdates,conn,onChange);

const UNAVAILABLE="unavailable";const UNKNOWN="unknown";const UNAVAILABLE_STATES=[UNAVAILABLE,UNKNOWN];

/**
 * https://bugs.chromium.org/p/v8/issues/detail?id=10682
 */function hasIntlGetCanonicalLocalesBug(){try{return new Intl.Locale('und-x-private').toString()==='x-private';}catch(e){return true;}}function shouldPolyfill$3(){return !('Locale'in Intl)||hasIntlGetCanonicalLocalesBug();}

/**
 * http://ecma-international.org/ecma-402/7.0/index.html#sec-canonicalizelocalelist
 * @param locales
 */function CanonicalizeLocaleList(locales){// TODO
return Intl.getCanonicalLocales(locales);}

var UNICODE_EXTENSION_SEQUENCE_REGEX=/-u(?:-[0-9a-z]{2,8})+/gi;function invariant(condition,message,Err){if(Err===void 0){Err=Error;}if(!condition){throw new Err(message);}}

/**
 * https://tc39.es/ecma402/#sec-bestavailablelocale
 * @param availableLocales
 * @param locale
 */function BestAvailableLocale(availableLocales,locale){var candidate=locale;while(true){if(availableLocales.has(candidate)){return candidate;}var pos=candidate.lastIndexOf('-');if(!~pos){return undefined;}if(pos>=2&&candidate[pos-2]==='-'){pos-=2;}candidate=candidate.slice(0,pos);}}

/**
 * https://tc39.es/ecma402/#sec-lookupmatcher
 * @param availableLocales
 * @param requestedLocales
 * @param getDefaultLocale
 */function LookupMatcher(availableLocales,requestedLocales,getDefaultLocale){var result={locale:''};for(var _i=0,requestedLocales_1=requestedLocales;_i<requestedLocales_1.length;_i++){var locale=requestedLocales_1[_i];var noExtensionLocale=locale.replace(UNICODE_EXTENSION_SEQUENCE_REGEX,'');var availableLocale=BestAvailableLocale(availableLocales,noExtensionLocale);if(availableLocale){result.locale=availableLocale;if(locale!==noExtensionLocale){result.extension=locale.slice(noExtensionLocale.length+1,locale.length);}return result;}}result.locale=getDefaultLocale();return result;}

/**
 * https://tc39.es/ecma402/#sec-bestfitmatcher
 * @param availableLocales
 * @param requestedLocales
 * @param getDefaultLocale
 */function BestFitMatcher(availableLocales,requestedLocales,getDefaultLocale){var minimizedAvailableLocaleMap={};var availableLocaleMap={};var canonicalizedLocaleMap={};var minimizedAvailableLocales=new Set();availableLocales.forEach(function(locale){var minimizedLocale=new Intl.Locale(locale).minimize().toString();var canonicalizedLocale=Intl.getCanonicalLocales(locale)[0]||locale;minimizedAvailableLocaleMap[minimizedLocale]=locale;availableLocaleMap[locale]=locale;canonicalizedLocaleMap[canonicalizedLocale]=locale;minimizedAvailableLocales.add(minimizedLocale);minimizedAvailableLocales.add(locale);minimizedAvailableLocales.add(canonicalizedLocale);});var foundLocale;for(var _i=0,requestedLocales_1=requestedLocales;_i<requestedLocales_1.length;_i++){var l=requestedLocales_1[_i];if(foundLocale){break;}var noExtensionLocale=l.replace(UNICODE_EXTENSION_SEQUENCE_REGEX,'');if(availableLocales.has(noExtensionLocale)){foundLocale=noExtensionLocale;break;}if(minimizedAvailableLocales.has(noExtensionLocale)){foundLocale=noExtensionLocale;break;}var locale=new Intl.Locale(noExtensionLocale);var maximizedRequestedLocale=locale.maximize().toString();var minimizedRequestedLocale=locale.minimize().toString();// Check minimized locale
if(minimizedAvailableLocales.has(minimizedRequestedLocale)){foundLocale=minimizedRequestedLocale;break;}// Lookup algo on maximized locale
foundLocale=BestAvailableLocale(minimizedAvailableLocales,maximizedRequestedLocale);}if(!foundLocale){return {locale:getDefaultLocale()};}return {locale:availableLocaleMap[foundLocale]||canonicalizedLocaleMap[foundLocale]||minimizedAvailableLocaleMap[foundLocale]||foundLocale};}

/**
 * https://tc39.es/ecma402/#sec-unicodeextensionvalue
 * @param extension
 * @param key
 */function UnicodeExtensionValue(extension,key){invariant(key.length===2,'key must have 2 elements');var size=extension.length;var searchValue="-".concat(key,"-");var pos=extension.indexOf(searchValue);if(pos!==-1){var start=pos+4;var end=start;var k=start;var done=false;while(!done){var e=extension.indexOf('-',k);var len=void 0;if(e===-1){len=size-k;}else {len=e-k;}if(len===2){done=true;}else if(e===-1){end=size;done=true;}else {end=e;k=e+1;}}return extension.slice(start,end);}searchValue="-".concat(key);pos=extension.indexOf(searchValue);if(pos!==-1&&pos+3===size){return '';}return undefined;}

/**
 * https://tc39.es/ecma402/#sec-resolvelocale
 */function ResolveLocale(availableLocales,requestedLocales,options,relevantExtensionKeys,localeData,getDefaultLocale){var matcher=options.localeMatcher;var r;if(matcher==='lookup'){r=LookupMatcher(availableLocales,requestedLocales,getDefaultLocale);}else {r=BestFitMatcher(availableLocales,requestedLocales,getDefaultLocale);}var foundLocale=r.locale;var result={locale:'',dataLocale:foundLocale};var supportedExtension='-u';for(var _i=0,relevantExtensionKeys_1=relevantExtensionKeys;_i<relevantExtensionKeys_1.length;_i++){var key=relevantExtensionKeys_1[_i];invariant(foundLocale in localeData,"Missing locale data for ".concat(foundLocale));var foundLocaleData=localeData[foundLocale];invariant(typeof foundLocaleData==='object'&&foundLocaleData!==null,"locale data ".concat(key," must be an object"));var keyLocaleData=foundLocaleData[key];invariant(Array.isArray(keyLocaleData),"keyLocaleData for ".concat(key," must be an array"));var value=keyLocaleData[0];invariant(typeof value==='string'||value===null,"value must be string or null but got ".concat(typeof value," in key ").concat(key));var supportedExtensionAddition='';if(r.extension){var requestedValue=UnicodeExtensionValue(r.extension,key);if(requestedValue!==undefined){if(requestedValue!==''){if(~keyLocaleData.indexOf(requestedValue)){value=requestedValue;supportedExtensionAddition="-".concat(key,"-").concat(value);}}else if(~requestedValue.indexOf('true')){value='true';supportedExtensionAddition="-".concat(key);}}}if(key in options){var optionsValue=options[key];invariant(typeof optionsValue==='string'||typeof optionsValue==='undefined'||optionsValue===null,'optionsValue must be String, Undefined or Null');if(~keyLocaleData.indexOf(optionsValue)){if(optionsValue!==value){value=optionsValue;supportedExtensionAddition='';}}}result[key]=value;supportedExtension+=supportedExtensionAddition;}if(supportedExtension.length>2){var privateIndex=foundLocale.indexOf('-x-');if(privateIndex===-1){foundLocale=foundLocale+supportedExtension;}else {var preExtension=foundLocale.slice(0,privateIndex);var postExtension=foundLocale.slice(privateIndex,foundLocale.length);foundLocale=preExtension+supportedExtension+postExtension;}foundLocale=Intl.getCanonicalLocales(foundLocale)[0];}result.locale=foundLocale;return result;}

/**
 * https://tc39.es/ecma402/#sec-lookupsupportedlocales
 * @param availableLocales
 * @param requestedLocales
 */function LookupSupportedLocales(availableLocales,requestedLocales){var subset=[];for(var _i=0,requestedLocales_1=requestedLocales;_i<requestedLocales_1.length;_i++){var locale=requestedLocales_1[_i];var noExtensionLocale=locale.replace(UNICODE_EXTENSION_SEQUENCE_REGEX,'');var availableLocale=BestAvailableLocale(availableLocales,noExtensionLocale);if(availableLocale){subset.push(availableLocale);}}return subset;}

function match(requestedLocales,availableLocales,defaultLocale,opts){var locales=availableLocales.reduce(function(all,l){all.add(l);return all;},new Set());return ResolveLocale(locales,CanonicalizeLocaleList(requestedLocales),{localeMatcher:(opts===null||opts===void 0?void 0:opts.algorithm)||'best fit'},[],{},function(){return defaultLocale;}).locale;}

var lib = /*#__PURE__*/Object.freeze({
  __proto__: null,
  match: match,
  LookupSupportedLocales: LookupSupportedLocales,
  ResolveLocale: ResolveLocale
});

// This file is generated from supported-locales-gen.ts
var supportedLocales$2=["af","ak","am","an","ar","ars","as","asa","ast","az","bal","be","bem","bez","bg","bho","bm","bn","bo","br","brx","bs","ca","ce","ceb","cgg","chr","ckb","cs","cy","da","de","doi","dsb","dv","dz","ee","el","en","eo","es","et","eu","fa","ff","fi","fil","fo","fr","fur","fy","ga","gd","gl","gsw","gu","guw","gv","ha","haw","he","hi","hnj","hr","hsb","hu","hy","ia","id","ig","ii","io","is","it","iu","ja","jbo","jgo","jmc","jv","jw","ka","kab","kaj","kcg","kde","kea","kk","kkj","kl","km","kn","ko","ks","ksb","ksh","ku","kw","ky","lag","lb","lg","lij","lkt","ln","lo","lt","lv","mas","mg","mgo","mk","ml","mn","mo","mr","ms","mt","my","nah","naq","nb","nd","ne","nl","nn","nnh","no","nqo","nr","nso","ny","nyn","om","or","os","osa","pa","pap","pcm","pl","prg","ps","pt-PT","pt","rm","ro","rof","ru","rwk","sah","saq","sat","sc","scn","sd","sdh","se","seh","ses","sg","sh","shi","si","sk","sl","sma","smi","smj","smn","sms","sn","so","sq","sr","ss","ssy","st","su","sv","sw","syr","ta","te","teo","th","ti","tig","tk","tl","tn","to","tpi","tr","ts","tzm","ug","uk","und","ur","uz","ve","vi","vo","vun","wa","wae","wo","xh","xog","yi","yo","yue","zh","zu"];

function supportedLocalesOf$2(locale){if(!locale){return true;}var locales=Array.isArray(locale)?locale:[locale];return Intl.PluralRules.supportedLocalesOf(locales).length===locales.length;}function shouldPolyfill$2(locale){if(locale===void 0){locale='en';}if(!('PluralRules'in Intl)||new Intl.PluralRules('en',{minimumFractionDigits:2}).select(1)==='one'||!supportedLocalesOf$2(locale)){return locale?match([locale],supportedLocales$2,'en'):undefined;}}

var commonjsGlobal = typeof globalThis !== 'undefined' ? globalThis : typeof window !== 'undefined' ? window : typeof global !== 'undefined' ? global : typeof self !== 'undefined' ? self : {};

function unwrapExports (x) {
	return x && x.__esModule && Object.prototype.hasOwnProperty.call(x, 'default') ? x['default'] : x;
}

function createCommonjsModule(fn, module) {
	return module = { exports: {} }, fn(module, module.exports), module.exports;
}

var CanonicalizeLocaleList_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.CanonicalizeLocaleList=void 0;/**
 * http://ecma-international.org/ecma-402/7.0/index.html#sec-canonicalizelocalelist
 * @param locales
 */function CanonicalizeLocaleList(locales){// TODO
return Intl.getCanonicalLocales(locales);}exports.CanonicalizeLocaleList=CanonicalizeLocaleList;});unwrapExports(CanonicalizeLocaleList_1);CanonicalizeLocaleList_1.CanonicalizeLocaleList;

var utils=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.invariant=exports.UNICODE_EXTENSION_SEQUENCE_REGEX=void 0;exports.UNICODE_EXTENSION_SEQUENCE_REGEX=/-u(?:-[0-9a-z]{2,8})+/gi;function invariant(condition,message,Err){if(Err===void 0){Err=Error;}if(!condition){throw new Err(message);}}exports.invariant=invariant;});unwrapExports(utils);utils.invariant;utils.UNICODE_EXTENSION_SEQUENCE_REGEX;

var BestAvailableLocale_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.BestAvailableLocale=void 0;/**
 * https://tc39.es/ecma402/#sec-bestavailablelocale
 * @param availableLocales
 * @param locale
 */function BestAvailableLocale(availableLocales,locale){var candidate=locale;while(true){if(availableLocales.has(candidate)){return candidate;}var pos=candidate.lastIndexOf('-');if(!~pos){return undefined;}if(pos>=2&&candidate[pos-2]==='-'){pos-=2;}candidate=candidate.slice(0,pos);}}exports.BestAvailableLocale=BestAvailableLocale;});unwrapExports(BestAvailableLocale_1);BestAvailableLocale_1.BestAvailableLocale;

var LookupMatcher_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.LookupMatcher=void 0;/**
 * https://tc39.es/ecma402/#sec-lookupmatcher
 * @param availableLocales
 * @param requestedLocales
 * @param getDefaultLocale
 */function LookupMatcher(availableLocales,requestedLocales,getDefaultLocale){var result={locale:''};for(var _i=0,requestedLocales_1=requestedLocales;_i<requestedLocales_1.length;_i++){var locale=requestedLocales_1[_i];var noExtensionLocale=locale.replace(utils.UNICODE_EXTENSION_SEQUENCE_REGEX,'');var availableLocale=(0, BestAvailableLocale_1.BestAvailableLocale)(availableLocales,noExtensionLocale);if(availableLocale){result.locale=availableLocale;if(locale!==noExtensionLocale){result.extension=locale.slice(noExtensionLocale.length+1,locale.length);}return result;}}result.locale=getDefaultLocale();return result;}exports.LookupMatcher=LookupMatcher;});unwrapExports(LookupMatcher_1);LookupMatcher_1.LookupMatcher;

var BestFitMatcher_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.BestFitMatcher=void 0;/**
 * https://tc39.es/ecma402/#sec-bestfitmatcher
 * @param availableLocales
 * @param requestedLocales
 * @param getDefaultLocale
 */function BestFitMatcher(availableLocales,requestedLocales,getDefaultLocale){var minimizedAvailableLocaleMap={};var availableLocaleMap={};var canonicalizedLocaleMap={};var minimizedAvailableLocales=new Set();availableLocales.forEach(function(locale){var minimizedLocale=new Intl.Locale(locale).minimize().toString();var canonicalizedLocale=Intl.getCanonicalLocales(locale)[0]||locale;minimizedAvailableLocaleMap[minimizedLocale]=locale;availableLocaleMap[locale]=locale;canonicalizedLocaleMap[canonicalizedLocale]=locale;minimizedAvailableLocales.add(minimizedLocale);minimizedAvailableLocales.add(locale);minimizedAvailableLocales.add(canonicalizedLocale);});var foundLocale;for(var _i=0,requestedLocales_1=requestedLocales;_i<requestedLocales_1.length;_i++){var l=requestedLocales_1[_i];if(foundLocale){break;}var noExtensionLocale=l.replace(utils.UNICODE_EXTENSION_SEQUENCE_REGEX,'');if(availableLocales.has(noExtensionLocale)){foundLocale=noExtensionLocale;break;}if(minimizedAvailableLocales.has(noExtensionLocale)){foundLocale=noExtensionLocale;break;}var locale=new Intl.Locale(noExtensionLocale);var maximizedRequestedLocale=locale.maximize().toString();var minimizedRequestedLocale=locale.minimize().toString();// Check minimized locale
if(minimizedAvailableLocales.has(minimizedRequestedLocale)){foundLocale=minimizedRequestedLocale;break;}// Lookup algo on maximized locale
foundLocale=(0, BestAvailableLocale_1.BestAvailableLocale)(minimizedAvailableLocales,maximizedRequestedLocale);}if(!foundLocale){return {locale:getDefaultLocale()};}return {locale:availableLocaleMap[foundLocale]||canonicalizedLocaleMap[foundLocale]||minimizedAvailableLocaleMap[foundLocale]||foundLocale};}exports.BestFitMatcher=BestFitMatcher;});unwrapExports(BestFitMatcher_1);BestFitMatcher_1.BestFitMatcher;

var UnicodeExtensionValue_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.UnicodeExtensionValue=void 0;/**
 * https://tc39.es/ecma402/#sec-unicodeextensionvalue
 * @param extension
 * @param key
 */function UnicodeExtensionValue(extension,key){(0, utils.invariant)(key.length===2,'key must have 2 elements');var size=extension.length;var searchValue="-".concat(key,"-");var pos=extension.indexOf(searchValue);if(pos!==-1){var start=pos+4;var end=start;var k=start;var done=false;while(!done){var e=extension.indexOf('-',k);var len=void 0;if(e===-1){len=size-k;}else {len=e-k;}if(len===2){done=true;}else if(e===-1){end=size;done=true;}else {end=e;k=e+1;}}return extension.slice(start,end);}searchValue="-".concat(key);pos=extension.indexOf(searchValue);if(pos!==-1&&pos+3===size){return '';}return undefined;}exports.UnicodeExtensionValue=UnicodeExtensionValue;});unwrapExports(UnicodeExtensionValue_1);UnicodeExtensionValue_1.UnicodeExtensionValue;

var ResolveLocale_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.ResolveLocale=void 0;/**
 * https://tc39.es/ecma402/#sec-resolvelocale
 */function ResolveLocale(availableLocales,requestedLocales,options,relevantExtensionKeys,localeData,getDefaultLocale){var matcher=options.localeMatcher;var r;if(matcher==='lookup'){r=(0, LookupMatcher_1.LookupMatcher)(availableLocales,requestedLocales,getDefaultLocale);}else {r=(0, BestFitMatcher_1.BestFitMatcher)(availableLocales,requestedLocales,getDefaultLocale);}var foundLocale=r.locale;var result={locale:'',dataLocale:foundLocale};var supportedExtension='-u';for(var _i=0,relevantExtensionKeys_1=relevantExtensionKeys;_i<relevantExtensionKeys_1.length;_i++){var key=relevantExtensionKeys_1[_i];(0, utils.invariant)(foundLocale in localeData,"Missing locale data for ".concat(foundLocale));var foundLocaleData=localeData[foundLocale];(0, utils.invariant)(typeof foundLocaleData==='object'&&foundLocaleData!==null,"locale data ".concat(key," must be an object"));var keyLocaleData=foundLocaleData[key];(0, utils.invariant)(Array.isArray(keyLocaleData),"keyLocaleData for ".concat(key," must be an array"));var value=keyLocaleData[0];(0, utils.invariant)(typeof value==='string'||value===null,"value must be string or null but got ".concat(typeof value," in key ").concat(key));var supportedExtensionAddition='';if(r.extension){var requestedValue=(0, UnicodeExtensionValue_1.UnicodeExtensionValue)(r.extension,key);if(requestedValue!==undefined){if(requestedValue!==''){if(~keyLocaleData.indexOf(requestedValue)){value=requestedValue;supportedExtensionAddition="-".concat(key,"-").concat(value);}}else if(~requestedValue.indexOf('true')){value='true';supportedExtensionAddition="-".concat(key);}}}if(key in options){var optionsValue=options[key];(0, utils.invariant)(typeof optionsValue==='string'||typeof optionsValue==='undefined'||optionsValue===null,'optionsValue must be String, Undefined or Null');if(~keyLocaleData.indexOf(optionsValue)){if(optionsValue!==value){value=optionsValue;supportedExtensionAddition='';}}}result[key]=value;supportedExtension+=supportedExtensionAddition;}if(supportedExtension.length>2){var privateIndex=foundLocale.indexOf('-x-');if(privateIndex===-1){foundLocale=foundLocale+supportedExtension;}else {var preExtension=foundLocale.slice(0,privateIndex);var postExtension=foundLocale.slice(privateIndex,foundLocale.length);foundLocale=preExtension+supportedExtension+postExtension;}foundLocale=Intl.getCanonicalLocales(foundLocale)[0];}result.locale=foundLocale;return result;}exports.ResolveLocale=ResolveLocale;});unwrapExports(ResolveLocale_1);ResolveLocale_1.ResolveLocale;

var LookupSupportedLocales_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.LookupSupportedLocales=void 0;/**
 * https://tc39.es/ecma402/#sec-lookupsupportedlocales
 * @param availableLocales
 * @param requestedLocales
 */function LookupSupportedLocales(availableLocales,requestedLocales){var subset=[];for(var _i=0,requestedLocales_1=requestedLocales;_i<requestedLocales_1.length;_i++){var locale=requestedLocales_1[_i];var noExtensionLocale=locale.replace(utils.UNICODE_EXTENSION_SEQUENCE_REGEX,'');var availableLocale=(0, BestAvailableLocale_1.BestAvailableLocale)(availableLocales,noExtensionLocale);if(availableLocale){subset.push(availableLocale);}}return subset;}exports.LookupSupportedLocales=LookupSupportedLocales;});unwrapExports(LookupSupportedLocales_1);LookupSupportedLocales_1.LookupSupportedLocales;

var intlLocalematcher=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.ResolveLocale=exports.LookupSupportedLocales=exports.match=void 0;function match(requestedLocales,availableLocales,defaultLocale,opts){var locales=availableLocales.reduce(function(all,l){all.add(l);return all;},new Set());return (0, ResolveLocale_1.ResolveLocale)(locales,(0, CanonicalizeLocaleList_1.CanonicalizeLocaleList)(requestedLocales),{localeMatcher:(opts===null||opts===void 0?void 0:opts.algorithm)||'best fit'},[],{},function(){return defaultLocale;}).locale;}exports.match=match;Object.defineProperty(exports,"LookupSupportedLocales",{enumerable:true,get:function(){return LookupSupportedLocales_1.LookupSupportedLocales;}});var ResolveLocale_2=ResolveLocale_1;Object.defineProperty(exports,"ResolveLocale",{enumerable:true,get:function(){return ResolveLocale_2.ResolveLocale;}});});unwrapExports(intlLocalematcher);var intlLocalematcher_1=intlLocalematcher.ResolveLocale;var intlLocalematcher_2=intlLocalematcher.LookupSupportedLocales;var intlLocalematcher_3=intlLocalematcher.match;

// This file is generated from supported-locales-gen.ts
var supportedLocales$1=["af-NA","af","agq","ak","am","ar-AE","ar-BH","ar-DJ","ar-DZ","ar-EG","ar-EH","ar-ER","ar-IL","ar-IQ","ar-JO","ar-KM","ar-KW","ar-LB","ar-LY","ar-MA","ar-MR","ar-OM","ar-PS","ar-QA","ar-SA","ar-SD","ar-SO","ar-SS","ar-SY","ar-TD","ar-TN","ar-YE","ar","as","asa","ast","az-Cyrl","az-Latn","az","bas","be-tarask","be","bem","bez","bg","bm","bn-IN","bn","bo-IN","bo","br","brx","bs-Cyrl","bs-Latn","bs","ca-AD","ca-ES-valencia","ca-FR","ca-IT","ca","ccp-IN","ccp","ce","ceb","cgg","chr","ckb-IR","ckb","cs","cy","da-GL","da","dav","de-AT","de-BE","de-CH","de-IT","de-LI","de-LU","de","dje","doi","dsb","dua","dyo","dz","ebu","ee-TG","ee","el-CY","el","en-001","en-150","en-AE","en-AG","en-AI","en-AS","en-AT","en-AU","en-BB","en-BE","en-BI","en-BM","en-BS","en-BW","en-BZ","en-CA","en-CC","en-CH","en-CK","en-CM","en-CX","en-CY","en-DE","en-DG","en-DK","en-DM","en-ER","en-FI","en-FJ","en-FK","en-FM","en-GB","en-GD","en-GG","en-GH","en-GI","en-GM","en-GU","en-GY","en-HK","en-IE","en-IL","en-IM","en-IN","en-IO","en-JE","en-JM","en-KE","en-KI","en-KN","en-KY","en-LC","en-LR","en-LS","en-MG","en-MH","en-MO","en-MP","en-MS","en-MT","en-MU","en-MW","en-MY","en-NA","en-NF","en-NG","en-NL","en-NR","en-NU","en-NZ","en-PG","en-PH","en-PK","en-PN","en-PR","en-PW","en-RW","en-SB","en-SC","en-SD","en-SE","en-SG","en-SH","en-SI","en-SL","en-SS","en-SX","en-SZ","en-TC","en-TK","en-TO","en-TT","en-TV","en-TZ","en-UG","en-UM","en-VC","en-VG","en-VI","en-VU","en-WS","en-ZA","en-ZM","en-ZW","en","eo","es-419","es-AR","es-BO","es-BR","es-BZ","es-CL","es-CO","es-CR","es-CU","es-DO","es-EA","es-EC","es-GQ","es-GT","es-HN","es-IC","es-MX","es-NI","es-PA","es-PE","es-PH","es-PR","es-PY","es-SV","es-US","es-UY","es-VE","es","et","eu","ewo","fa-AF","fa","ff-Adlm-BF","ff-Adlm-CM","ff-Adlm-GH","ff-Adlm-GM","ff-Adlm-GW","ff-Adlm-LR","ff-Adlm-MR","ff-Adlm-NE","ff-Adlm-NG","ff-Adlm-SL","ff-Adlm-SN","ff-Adlm","ff-Latn-BF","ff-Latn-CM","ff-Latn-GH","ff-Latn-GM","ff-Latn-GN","ff-Latn-GW","ff-Latn-LR","ff-Latn-MR","ff-Latn-NE","ff-Latn-NG","ff-Latn-SL","ff-Latn","ff","fi","fil","fo-DK","fo","fr-BE","fr-BF","fr-BI","fr-BJ","fr-BL","fr-CA","fr-CD","fr-CF","fr-CG","fr-CH","fr-CI","fr-CM","fr-DJ","fr-DZ","fr-GA","fr-GF","fr-GN","fr-GP","fr-GQ","fr-HT","fr-KM","fr-LU","fr-MA","fr-MC","fr-MF","fr-MG","fr-ML","fr-MQ","fr-MR","fr-MU","fr-NC","fr-NE","fr-PF","fr-PM","fr-RE","fr-RW","fr-SC","fr-SN","fr-SY","fr-TD","fr-TG","fr-TN","fr-VU","fr-WF","fr-YT","fr","fur","fy","ga-GB","ga","gd","gl","gsw-FR","gsw-LI","gsw","gu","guz","gv","ha-GH","ha-NE","ha","haw","he","hi","hr-BA","hr","hsb","hu","hy","ia","id","ig","ii","is","it-CH","it-SM","it-VA","it","ja","jgo","jmc","jv","ka","kab","kam","kde","kea","kgp","khq","ki","kk","kkj","kl","kln","km","kn","ko-KP","ko","kok","ks-Arab","ks","ksb","ksf","ksh","ku","kw","ky","lag","lb","lg","lkt","ln-AO","ln-CF","ln-CG","ln","lo","lrc-IQ","lrc","lt","lu","luo","luy","lv","mai","mas-TZ","mas","mer","mfe","mg","mgh","mgo","mi","mk","ml","mn","mni-Beng","mni","mr","ms-BN","ms-ID","ms-SG","ms","mt","mua","my","mzn","naq","nb-SJ","nb","nd","nds-NL","nds","ne-IN","ne","nl-AW","nl-BE","nl-BQ","nl-CW","nl-SR","nl-SX","nl","nmg","nn","nnh","no","nus","nyn","om-KE","om","or","os-RU","os","pa-Arab","pa-Guru","pa","pcm","pl","ps-PK","ps","pt-AO","pt-CH","pt-CV","pt-GQ","pt-GW","pt-LU","pt-MO","pt-MZ","pt-PT","pt-ST","pt-TL","pt","qu-BO","qu-EC","qu","rm","rn","ro-MD","ro","rof","ru-BY","ru-KG","ru-KZ","ru-MD","ru-UA","ru","rw","rwk","sa","sah","saq","sat-Olck","sat","sbp","sc","sd-Arab","sd-Deva","sd","se-FI","se-SE","se","seh","ses","sg","shi-Latn","shi-Tfng","shi","si","sk","sl","smn","sn","so-DJ","so-ET","so-KE","so","sq-MK","sq-XK","sq","sr-Cyrl-BA","sr-Cyrl-ME","sr-Cyrl-XK","sr-Cyrl","sr-Latn-BA","sr-Latn-ME","sr-Latn-XK","sr-Latn","sr","su-Latn","su","sv-AX","sv-FI","sv","sw-CD","sw-KE","sw-UG","sw","ta-LK","ta-MY","ta-SG","ta","te","teo-KE","teo","tg","th","ti-ER","ti","tk","to","tr-CY","tr","tt","twq","tzm","ug","uk","und","ur-IN","ur","uz-Arab","uz-Cyrl","uz-Latn","uz","vai-Latn","vai-Vaii","vai","vi","vun","wae","wo","xh","xog","yav","yi","yo-BJ","yo","yrl-CO","yrl-VE","yrl","yue-Hans","yue-Hant","yue","zgh","zh-Hans-HK","zh-Hans-MO","zh-Hans-SG","zh-Hans","zh-Hant-HK","zh-Hant-MO","zh-Hant","zh","zu"];

function supportedLocalesOf$1(locale){if(!locale){return true;}var locales=Array.isArray(locale)?locale:[locale];return Intl.RelativeTimeFormat.supportedLocalesOf(locales).length===locales.length;}function hasResolvedOptionsNumberingSystem(locale){try{return 'numberingSystem'in new Intl.RelativeTimeFormat(locale||'en',{numeric:'auto'}).resolvedOptions();}catch(_){return false;}}function shouldPolyfill$1(locale){if(locale===void 0){locale='en';}if(!('RelativeTimeFormat'in Intl)||!supportedLocalesOf$1(locale)||!hasResolvedOptionsNumberingSystem(locale)){return intlLocalematcher_3([locale],supportedLocales$1,'en');}}

// This file is generated from supported-locales-gen.ts
var supportedLocales=["af-NA","af","agq","ak","am","ar-AE","ar-BH","ar-DJ","ar-DZ","ar-EG","ar-EH","ar-ER","ar-IL","ar-IQ","ar-JO","ar-KM","ar-KW","ar-LB","ar-LY","ar-MA","ar-MR","ar-OM","ar-PS","ar-QA","ar-SA","ar-SD","ar-SO","ar-SS","ar-SY","ar-TD","ar-TN","ar-YE","ar","as","asa","ast","az-Cyrl","az-Latn","az","bas","be-tarask","be","bem","bez","bg","bm","bn-IN","bn","bo-IN","bo","br","brx","bs-Cyrl","bs-Latn","bs","ca-AD","ca-ES-valencia","ca-FR","ca-IT","ca","ccp-IN","ccp","ce","ceb","cgg","chr","ckb-IR","ckb","cs","cy","da-GL","da","dav","de-AT","de-BE","de-CH","de-IT","de-LI","de-LU","de","dje","doi","dsb","dua","dyo","dz","ebu","ee-TG","ee","el-CY","el","en-001","en-150","en-AE","en-AG","en-AI","en-AS","en-AT","en-AU","en-BB","en-BE","en-BI","en-BM","en-BS","en-BW","en-BZ","en-CA","en-CC","en-CH","en-CK","en-CM","en-CX","en-CY","en-DE","en-DG","en-DK","en-DM","en-ER","en-FI","en-FJ","en-FK","en-FM","en-GB","en-GD","en-GG","en-GH","en-GI","en-GM","en-GU","en-GY","en-HK","en-IE","en-IL","en-IM","en-IN","en-IO","en-JE","en-JM","en-KE","en-KI","en-KN","en-KY","en-LC","en-LR","en-LS","en-MG","en-MH","en-MO","en-MP","en-MS","en-MT","en-MU","en-MW","en-MY","en-NA","en-NF","en-NG","en-NL","en-NR","en-NU","en-NZ","en-PG","en-PH","en-PK","en-PN","en-PR","en-PW","en-RW","en-SB","en-SC","en-SD","en-SE","en-SG","en-SH","en-SI","en-SL","en-SS","en-SX","en-SZ","en-TC","en-TK","en-TO","en-TT","en-TV","en-TZ","en-UG","en-UM","en-VC","en-VG","en-VI","en-VU","en-WS","en-ZA","en-ZM","en-ZW","en","eo","es-419","es-AR","es-BO","es-BR","es-BZ","es-CL","es-CO","es-CR","es-CU","es-DO","es-EA","es-EC","es-GQ","es-GT","es-HN","es-IC","es-MX","es-NI","es-PA","es-PE","es-PH","es-PR","es-PY","es-SV","es-US","es-UY","es-VE","es","et","eu","ewo","fa-AF","fa","ff-Adlm-BF","ff-Adlm-CM","ff-Adlm-GH","ff-Adlm-GM","ff-Adlm-GW","ff-Adlm-LR","ff-Adlm-MR","ff-Adlm-NE","ff-Adlm-NG","ff-Adlm-SL","ff-Adlm-SN","ff-Adlm","ff-Latn-BF","ff-Latn-CM","ff-Latn-GH","ff-Latn-GM","ff-Latn-GN","ff-Latn-GW","ff-Latn-LR","ff-Latn-MR","ff-Latn-NE","ff-Latn-NG","ff-Latn-SL","ff-Latn","ff","fi","fil","fo-DK","fo","fr-BE","fr-BF","fr-BI","fr-BJ","fr-BL","fr-CA","fr-CD","fr-CF","fr-CG","fr-CH","fr-CI","fr-CM","fr-DJ","fr-DZ","fr-GA","fr-GF","fr-GN","fr-GP","fr-GQ","fr-HT","fr-KM","fr-LU","fr-MA","fr-MC","fr-MF","fr-MG","fr-ML","fr-MQ","fr-MR","fr-MU","fr-NC","fr-NE","fr-PF","fr-PM","fr-RE","fr-RW","fr-SC","fr-SN","fr-SY","fr-TD","fr-TG","fr-TN","fr-VU","fr-WF","fr-YT","fr","fur","fy","ga-GB","ga","gd","gl","gsw-FR","gsw-LI","gsw","gu","guz","gv","ha-GH","ha-NE","ha","haw","he","hi","hr-BA","hr","hsb","hu","hy","ia","id","ig","ii","is","it-CH","it-SM","it-VA","it","ja","jgo","jmc","jv","ka","kab","kam","kde","kea","kgp","khq","ki","kk","kkj","kl","kln","km","kn","ko-KP","ko","kok","ks-Arab","ks","ksb","ksf","ksh","ku","kw","ky","lag","lb","lg","lkt","ln-AO","ln-CF","ln-CG","ln","lo","lrc-IQ","lrc","lt","lu","luo","luy","lv","mai","mas-TZ","mas","mer","mfe","mg","mgh","mgo","mi","mk","ml","mn","mni-Beng","mni","mr","ms-BN","ms-ID","ms-SG","ms","mt","mua","my","mzn","naq","nb-SJ","nb","nd","nds-NL","nds","ne-IN","ne","nl-AW","nl-BE","nl-BQ","nl-CW","nl-SR","nl-SX","nl","nmg","nn","nnh","no","nus","nyn","om-KE","om","or","os-RU","os","pa-Arab","pa-Guru","pa","pcm","pl","ps-PK","ps","pt-AO","pt-CH","pt-CV","pt-GQ","pt-GW","pt-LU","pt-MO","pt-MZ","pt-PT","pt-ST","pt-TL","pt","qu-BO","qu-EC","qu","rm","rn","ro-MD","ro","rof","ru-BY","ru-KG","ru-KZ","ru-MD","ru-UA","ru","rw","rwk","sa","sah","saq","sat-Olck","sat","sbp","sc","sd-Arab","sd-Deva","sd","se-FI","se-SE","se","seh","ses","sg","shi-Latn","shi-Tfng","shi","si","sk","sl","smn","sn","so-DJ","so-ET","so-KE","so","sq-MK","sq-XK","sq","sr-Cyrl-BA","sr-Cyrl-ME","sr-Cyrl-XK","sr-Cyrl","sr-Latn-BA","sr-Latn-ME","sr-Latn-XK","sr-Latn","sr","su-Latn","su","sv-AX","sv-FI","sv","sw-CD","sw-KE","sw-UG","sw","ta-LK","ta-MY","ta-SG","ta","te","teo-KE","teo","tg","th","ti-ER","ti","tk","to","tr-CY","tr","tt","twq","tzm","ug","uk","und","ur-IN","ur","uz-Arab","uz-Cyrl","uz-Latn","uz","vai-Latn","vai-Vaii","vai","vi","vun","wae","wo","xh","xog","yav","yi","yo-BJ","yo","yrl-CO","yrl-VE","yrl","yue-Hans","yue-Hant","yue","zgh","zh-Hans-HK","zh-Hans-MO","zh-Hans-SG","zh-Hans","zh-Hant-HK","zh-Hant-MO","zh-Hant","zh","zu"];

function supportsDateStyle(){try{return !!new Intl.DateTimeFormat(undefined,{dateStyle:'short'}).resolvedOptions().dateStyle;}catch(e){return false;}}/**
 * https://bugs.chromium.org/p/chromium/issues/detail?id=865351
 */function hasChromeLt71Bug(){try{return new Intl.DateTimeFormat('en',{hourCycle:'h11',hour:'numeric'}).formatToParts(0)[2].type!=='dayPeriod';}catch(e){return false;}}/**
 * Node 14's version of Intl.DateTimeFormat does not throw
 * when dateStyle/timeStyle is used with other options.
 * This was fixed in newer V8 versions
 */function hasUnthrownDateTimeStyleBug(){try{return !!new Intl.DateTimeFormat('en',{dateStyle:'short',hour:'numeric'}).format(new Date(0));}catch(e){return false;}}function supportedLocalesOf(locale){if(!locale){return true;}var locales=Array.isArray(locale)?locale:[locale];return Intl.DateTimeFormat.supportedLocalesOf(locales).length===locales.length;}function shouldPolyfill(locale){if(locale===void 0){locale='en';}if(!('DateTimeFormat'in Intl)||!('formatToParts'in Intl.DateTimeFormat.prototype)||!('formatRange'in Intl.DateTimeFormat.prototype)||hasChromeLt71Bug()||hasUnthrownDateTimeStyleBug()||!supportsDateStyle()||!supportedLocalesOf(locale)){return locale?intlLocalematcher_3([locale],supportedLocales,'en'):undefined;}}

let NumberFormat;(function(NumberFormat){NumberFormat["language"]="language";NumberFormat["system"]="system";NumberFormat["comma_decimal"]="comma_decimal";NumberFormat["decimal_comma"]="decimal_comma";NumberFormat["space_comma"]="space_comma";NumberFormat["none"]="none";})(NumberFormat||(NumberFormat={}));let TimeFormat;(function(TimeFormat){TimeFormat["language"]="language";TimeFormat["system"]="system";TimeFormat["am_pm"]="12";TimeFormat["twenty_four"]="24";})(TimeFormat||(TimeFormat={}));

var translationMetadata$1 = {};

const translationMetadata=translationMetadata$1;

const STORAGE=window.localStorage||{};// Store loaded translations in memory so translations are available immediately
const LOCALE_LOOKUP={"zh-cn":"zh-Hans","zh-sg":"zh-Hans","zh-my":"zh-Hans","zh-tw":"zh-Hant","zh-hk":"zh-Hant","zh-mo":"zh-Hant",zh:"zh-Hant"// all other Chinese locales map to Traditional Chinese
};/**
 * Search for a matching translation from most specific to general
 */function findAvailableLanguage(language){// In most case, the language has the same format with our translation meta data
if(language in translationMetadata.translations){return language;}// Perform case-insenstive comparison since browser isn't required to
// report languages with specific cases.
const langLower=language.toLowerCase();if(langLower in LOCALE_LOOKUP){return LOCALE_LOOKUP[langLower];}const translation=Object.keys(translationMetadata.translations).find(lang=>lang.toLowerCase()===langLower);if(translation){return translation;}if(language.includes("-")){return findAvailableLanguage(language.split("-")[0]);}return undefined;}/**
 * Get browser specific language
 */function getLocalLanguage(){let language=null;if(STORAGE.selectedLanguage){try{const stored=JSON.parse(STORAGE.selectedLanguage);if(stored){language=findAvailableLanguage(stored);if(language){return language;}}}catch(err){// Ignore parsing error.
}}if(navigator.languages){for(const locale of navigator.languages){language=findAvailableLanguage(locale);if(language){return language;}}}language=findAvailableLanguage(navigator.language);if(language){return language;}// Final fallback
return "en";}

const loadedPolyfillLocale=new Set();const polyfills=[];if(__BUILD__==="latest"){if(shouldPolyfill$3()){polyfills.push(import('./polyfill-dev.js'));}if(shouldPolyfill$2()){polyfills.push(import('./polyfill-dev2.js'));polyfills.push(import('./en-dev.js'));}if(shouldPolyfill$1()){polyfills.push(import('./polyfill-dev3.js'));}if(shouldPolyfill()){polyfills.push(import('./polyfill-dev4.js'));polyfills.push(import('./add-all-tz-dev.js'));}}const polyfillsLoaded=polyfills.length===0?undefined:Promise.all(polyfills).then(()=>// Load the default language
loadPolyfillLocales(getLocalLanguage()));const loadPolyfillLocales=async language=>{if(loadedPolyfillLocale.has(language)){return;}loadedPolyfillLocale.add(language);try{if(Intl.NumberFormat&&// @ts-ignore
typeof Intl.NumberFormat.__addLocaleData==="function"){const result=await fetch(`/static/locale-data/intl-numberformat/${language}.json`);// @ts-ignore
Intl.NumberFormat.__addLocaleData(await result.json());}if(// @ts-expect-error
Intl.RelativeTimeFormat&&// @ts-ignore
typeof Intl.RelativeTimeFormat.__addLocaleData==="function"){const result=await fetch(`/static/locale-data/intl-relativetimeformat/${language}.json`);// @ts-ignore
Intl.RelativeTimeFormat.__addLocaleData(await result.json());}if(Intl.DateTimeFormat&&// @ts-ignore
typeof Intl.DateTimeFormat.__addLocaleData==="function"){const result=await fetch(`/static/locale-data/intl-datetimeformat/${language}.json`);// @ts-ignore
Intl.DateTimeFormat.__addLocaleData(await result.json());}}catch(_e){// Ignore
}};

if(__BUILD__==="latest"&&polyfillsLoaded){await polyfillsLoaded;}// Tuesday, August 10
const formatDateWeekday=(dateObj,locale)=>formatDateWeekdayMem(locale).format(dateObj);const formatDateWeekdayMem=memoizeOne(locale=>new Intl.DateTimeFormat(locale.language,{weekday:"long",month:"long",day:"numeric"}));// August 10, 2021
const formatDate=(dateObj,locale)=>formatDateMem(locale).format(dateObj);const formatDateMem=memoizeOne(locale=>new Intl.DateTimeFormat(locale.language,{year:"numeric",month:"long",day:"numeric"}));// 10/08/2021
const formatDateNumeric=(dateObj,locale)=>formatDateNumericMem(locale).format(dateObj);const formatDateNumericMem=memoizeOne(locale=>new Intl.DateTimeFormat(locale.language,{year:"numeric",month:"numeric",day:"numeric"}));// Aug 10
const formatDateShort=(dateObj,locale)=>formatDateShortMem(locale).format(dateObj);const formatDateShortMem=memoizeOne(locale=>new Intl.DateTimeFormat(locale.language,{day:"numeric",month:"short"}));// August 2021
const formatDateMonthYear=(dateObj,locale)=>formatDateMonthYearMem(locale).format(dateObj);const formatDateMonthYearMem=memoizeOne(locale=>new Intl.DateTimeFormat(locale.language,{month:"long",year:"numeric"}));// August
const formatDateMonth=(dateObj,locale)=>formatDateMonthMem(locale).format(dateObj);const formatDateMonthMem=memoizeOne(locale=>new Intl.DateTimeFormat(locale.language,{month:"long"}));// 2021
const formatDateYear=(dateObj,locale)=>formatDateYearMem(locale).format(dateObj);const formatDateYearMem=memoizeOne(locale=>new Intl.DateTimeFormat(locale.language,{year:"numeric"}));

const useAmPm=memoizeOne(locale=>{if(locale.time_format===TimeFormat.language||locale.time_format===TimeFormat.system){const testLanguage=locale.time_format===TimeFormat.language?locale.language:undefined;const test=new Date().toLocaleString(testLanguage);return test.includes("AM")||test.includes("PM");}return locale.time_format===TimeFormat.am_pm;});

if(__BUILD__==="latest"&&polyfillsLoaded){await polyfillsLoaded;}// August 9, 2021, 8:23 AM
const formatDateTime=(dateObj,locale)=>formatDateTimeMem(locale).format(dateObj);const formatDateTimeMem=memoizeOne(locale=>new Intl.DateTimeFormat(locale.language==="en"&&!useAmPm(locale)?"en-u-hc-h23":locale.language,{year:"numeric",month:"long",day:"numeric",hour:useAmPm(locale)?"numeric":"2-digit",minute:"2-digit",hour12:useAmPm(locale)}));// August 9, 2021, 8:23:15 AM
const formatDateTimeWithSeconds=(dateObj,locale)=>formatDateTimeWithSecondsMem(locale).format(dateObj);const formatDateTimeWithSecondsMem=memoizeOne(locale=>new Intl.DateTimeFormat(locale.language==="en"&&!useAmPm(locale)?"en-u-hc-h23":locale.language,{year:"numeric",month:"long",day:"numeric",hour:useAmPm(locale)?"numeric":"2-digit",minute:"2-digit",second:"2-digit",hour12:useAmPm(locale)}));// 9/8/2021, 8:23 AM
memoizeOne(locale=>new Intl.DateTimeFormat(locale.language==="en"&&!useAmPm(locale)?"en-u-hc-h23":locale.language,{year:"numeric",month:"numeric",day:"numeric",hour:"numeric",minute:"2-digit",hour12:useAmPm(locale)}));

const round=(value,precision=2)=>Math.round(value*10**precision)/10**precision;

/**
 * Returns true if the entity is considered numeric based on the attributes it has
 * @param stateObj The entity state object
 */const isNumericState=stateObj=>!!stateObj.attributes.unit_of_measurement||!!stateObj.attributes.state_class;const numberFormatToLocale=localeOptions=>{switch(localeOptions.number_format){case NumberFormat.comma_decimal:return ["en-US","en"];// Use United States with fallback to English formatting 1,234,567.89
case NumberFormat.decimal_comma:return ["de","es","it"];// Use German with fallback to Spanish then Italian formatting 1.234.567,89
case NumberFormat.space_comma:return ["fr","sv","cs"];// Use French with fallback to Swedish and Czech formatting 1 234 567,89
case NumberFormat.system:return undefined;default:return localeOptions.language;}};/**
 * Formats a number based on the user's preference with thousands separator(s) and decimal character for better legibility.
 *
 * @param num The number to format
 * @param locale The user-selected language and number format, from `hass.locale`
 * @param options Intl.NumberFormatOptions to use
 */const formatNumber=(num,localeOptions,options)=>{const locale=localeOptions?numberFormatToLocale(localeOptions):undefined;// Polyfill for Number.isNaN, which is more reliable than the global isNaN()
Number.isNaN=Number.isNaN||function isNaN(input){return typeof input==="number"&&isNaN(input);};if((localeOptions===null||localeOptions===void 0?void 0:localeOptions.number_format)!==NumberFormat.none&&!Number.isNaN(Number(num))&&Intl){try{return new Intl.NumberFormat(locale,getDefaultFormatOptions(num,options)).format(Number(num));}catch(err){// Don't fail when using "TEST" language
// eslint-disable-next-line no-console
console.error(err);return new Intl.NumberFormat(undefined,getDefaultFormatOptions(num,options)).format(Number(num));}}if(typeof num==="string"){return num;}return `${round(num,options===null||options===void 0?void 0:options.maximumFractionDigits).toString()}${(options===null||options===void 0?void 0:options.style)==="currency"?` ${options.currency}`:""}`;};/**
 * Generates default options for Intl.NumberFormat
 * @param num The number to be formatted
 * @param options The Intl.NumberFormatOptions that should be included in the returned options
 */const getDefaultFormatOptions=(num,options)=>{const defaultOptions={maximumFractionDigits:2,...options};if(typeof num!=="string"){return defaultOptions;}// Keep decimal trailing zeros if they are present in a string numeric value
if(!options||!options.minimumFractionDigits&&!options.maximumFractionDigits){const digits=num.indexOf(".")>-1?num.split(".")[1].length:0;defaultOptions.minimumFractionDigits=digits;defaultOptions.maximumFractionDigits=digits;}return defaultOptions;};

const computeStateDomain=stateObj=>computeDomain(stateObj.entity_id);

const supportsFeature=(stateObj,feature)=>// eslint-disable-next-line no-bitwise
(stateObj.attributes.supported_features&feature)!==0;

// https://developer.apple.com/design/human-interface-guidelines/ios/user-interaction/feedback/#haptics
// Implementors on platforms other than iOS should attempt to match the patterns (shown in HIG) as closely as possible.
const forwardHaptic=hapticType=>{fireEvent(window,"haptic",hapticType);};

/**
 * @license
 * Copyright 2018 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */ /** CSS classes used by the switch. */var cssClasses={/** Class used for a switch that is in the "checked" (on) position. */CHECKED:'mdc-switch--checked',/** Class used for a switch that is disabled. */DISABLED:'mdc-switch--disabled'};/** String constants used by the switch. */var strings={/** Aria attribute for checked or unchecked state of switch */ARIA_CHECKED_ATTR:'aria-checked',/** A CSS selector used to locate the native HTML control for the switch.  */NATIVE_CONTROL_SELECTOR:'.mdc-switch__native-control',/** A CSS selector used to locate the ripple surface element for the switch. */RIPPLE_SURFACE_SELECTOR:'.mdc-switch__thumb-underlay'};

var MDCSwitchFoundation=/** @class */function(_super){__extends(MDCSwitchFoundation,_super);function MDCSwitchFoundation(adapter){return _super.call(this,__assign(__assign({},MDCSwitchFoundation.defaultAdapter),adapter))||this;}Object.defineProperty(MDCSwitchFoundation,"strings",{/** The string constants used by the switch. */get:function(){return strings;},enumerable:false,configurable:true});Object.defineProperty(MDCSwitchFoundation,"cssClasses",{/** The CSS classes used by the switch. */get:function(){return cssClasses;},enumerable:false,configurable:true});Object.defineProperty(MDCSwitchFoundation,"defaultAdapter",{/** The default Adapter for the switch. */get:function(){return {addClass:function(){return undefined;},removeClass:function(){return undefined;},setNativeControlChecked:function(){return undefined;},setNativeControlDisabled:function(){return undefined;},setNativeControlAttr:function(){return undefined;}};},enumerable:false,configurable:true});/** Sets the checked state of the switch. */MDCSwitchFoundation.prototype.setChecked=function(checked){this.adapter.setNativeControlChecked(checked);this.updateAriaChecked(checked);this.updateCheckedStyling(checked);};/** Sets the disabled state of the switch. */MDCSwitchFoundation.prototype.setDisabled=function(disabled){this.adapter.setNativeControlDisabled(disabled);if(disabled){this.adapter.addClass(cssClasses.DISABLED);}else {this.adapter.removeClass(cssClasses.DISABLED);}};/** Handles the change event for the switch native control. */MDCSwitchFoundation.prototype.handleChange=function(evt){var nativeControl=evt.target;this.updateAriaChecked(nativeControl.checked);this.updateCheckedStyling(nativeControl.checked);};/** Updates the styling of the switch based on its checked state. */MDCSwitchFoundation.prototype.updateCheckedStyling=function(checked){if(checked){this.adapter.addClass(cssClasses.CHECKED);}else {this.adapter.removeClass(cssClasses.CHECKED);}};MDCSwitchFoundation.prototype.updateAriaChecked=function(checked){this.adapter.setNativeControlAttr(strings.ARIA_CHECKED_ATTR,""+!!checked);};return MDCSwitchFoundation;}(MDCFoundation);var MDCSwitchFoundation$1 = MDCSwitchFoundation;

class SwitchBase extends BaseElement{constructor(){super(...arguments);this.checked=false;this.disabled=false;this.shouldRenderRipple=false;this.mdcFoundationClass=MDCSwitchFoundation$1;this.rippleHandlers=new RippleHandlers(()=>{this.shouldRenderRipple=true;return this.ripple;});}changeHandler(e){this.mdcFoundation.handleChange(e);// catch "click" event and sync properties
this.checked=this.formElement.checked;}createAdapter(){return Object.assign(Object.assign({},addHasRemoveClass(this.mdcRoot)),{setNativeControlChecked:checked=>{this.formElement.checked=checked;},setNativeControlDisabled:disabled=>{this.formElement.disabled=disabled;},setNativeControlAttr:(attr,value)=>{this.formElement.setAttribute(attr,value);}});}renderRipple(){return this.shouldRenderRipple?$`
        <mwc-ripple
          .accent="${this.checked}"
          .disabled="${this.disabled}"
          unbounded>
        </mwc-ripple>`:'';}focus(){const formElement=this.formElement;if(formElement){this.rippleHandlers.startFocus();formElement.focus();}}blur(){const formElement=this.formElement;if(formElement){this.rippleHandlers.endFocus();formElement.blur();}}click(){if(this.formElement&&!this.disabled){this.formElement.focus();this.formElement.click();}}firstUpdated(){super.firstUpdated();if(this.shadowRoot){this.mdcRoot.addEventListener('change',e=>{this.dispatchEvent(new Event('change',e));});}}render(){return $`
      <div class="mdc-switch">
        <div class="mdc-switch__track"></div>
        <div class="mdc-switch__thumb-underlay">
          ${this.renderRipple()}
          <div class="mdc-switch__thumb">
            <input
              type="checkbox"
              id="basic-switch"
              class="mdc-switch__native-control"
              role="switch"
              aria-label="${l$1(this.ariaLabel)}"
              aria-labelledby="${l$1(this.ariaLabelledBy)}"
              @change="${this.changeHandler}"
              @focus="${this.handleRippleFocus}"
              @blur="${this.handleRippleBlur}"
              @mousedown="${this.handleRippleMouseDown}"
              @mouseenter="${this.handleRippleMouseEnter}"
              @mouseleave="${this.handleRippleMouseLeave}"
              @touchstart="${this.handleRippleTouchStart}"
              @touchend="${this.handleRippleDeactivate}"
              @touchcancel="${this.handleRippleDeactivate}">
          </div>
        </div>
      </div>`;}handleRippleMouseDown(event){const onUp=()=>{window.removeEventListener('mouseup',onUp);this.handleRippleDeactivate();};window.addEventListener('mouseup',onUp);this.rippleHandlers.startPress(event);}handleRippleTouchStart(event){this.rippleHandlers.startPress(event);}handleRippleDeactivate(){this.rippleHandlers.endPress();}handleRippleMouseEnter(){this.rippleHandlers.startHover();}handleRippleMouseLeave(){this.rippleHandlers.endHover();}handleRippleFocus(){this.rippleHandlers.startFocus();}handleRippleBlur(){this.rippleHandlers.endFocus();}}__decorate([e$1({type:Boolean}),observer(function(value){this.mdcFoundation.setChecked(value);})],SwitchBase.prototype,"checked",void 0);__decorate([e$1({type:Boolean}),observer(function(value){this.mdcFoundation.setDisabled(value);})],SwitchBase.prototype,"disabled",void 0);__decorate([ariaProperty,e$1({attribute:'aria-label'})],SwitchBase.prototype,"ariaLabel",void 0);__decorate([ariaProperty,e$1({attribute:'aria-labelledby'})],SwitchBase.prototype,"ariaLabelledBy",void 0);__decorate([i$1('.mdc-switch')],SwitchBase.prototype,"mdcRoot",void 0);__decorate([i$1('input')],SwitchBase.prototype,"formElement",void 0);__decorate([e$2('mwc-ripple')],SwitchBase.prototype,"ripple",void 0);__decorate([t()],SwitchBase.prototype,"shouldRenderRipple",void 0);__decorate([e$3({passive:true})],SwitchBase.prototype,"handleRippleMouseDown",null);__decorate([e$3({passive:true})],SwitchBase.prototype,"handleRippleTouchStart",null);

const styles=r$1`.mdc-switch__thumb-underlay{left:-14px;right:initial;top:-17px;width:48px;height:48px}[dir=rtl] .mdc-switch__thumb-underlay,.mdc-switch__thumb-underlay[dir=rtl]{left:initial;right:-14px}.mdc-switch__native-control{width:64px;height:48px}.mdc-switch{display:inline-block;position:relative;outline:none;user-select:none}.mdc-switch.mdc-switch--checked .mdc-switch__track{background-color:#018786;background-color:var(--mdc-theme-secondary, #018786)}.mdc-switch.mdc-switch--checked .mdc-switch__thumb{background-color:#018786;background-color:var(--mdc-theme-secondary, #018786);border-color:#018786;border-color:var(--mdc-theme-secondary, #018786)}.mdc-switch:not(.mdc-switch--checked) .mdc-switch__track{background-color:#000;background-color:var(--mdc-theme-on-surface, #000)}.mdc-switch:not(.mdc-switch--checked) .mdc-switch__thumb{background-color:#fff;background-color:var(--mdc-theme-surface, #fff);border-color:#fff;border-color:var(--mdc-theme-surface, #fff)}.mdc-switch__native-control{left:0;right:initial;position:absolute;top:0;margin:0;opacity:0;cursor:pointer;pointer-events:auto;transition:transform 90ms cubic-bezier(0.4, 0, 0.2, 1)}[dir=rtl] .mdc-switch__native-control,.mdc-switch__native-control[dir=rtl]{left:initial;right:0}.mdc-switch__track{box-sizing:border-box;width:36px;height:14px;border:1px solid transparent;border-radius:7px;opacity:.38;transition:opacity 90ms cubic-bezier(0.4, 0, 0.2, 1),background-color 90ms cubic-bezier(0.4, 0, 0.2, 1),border-color 90ms cubic-bezier(0.4, 0, 0.2, 1)}.mdc-switch__thumb-underlay{display:flex;position:absolute;align-items:center;justify-content:center;transform:translateX(0);transition:transform 90ms cubic-bezier(0.4, 0, 0.2, 1),background-color 90ms cubic-bezier(0.4, 0, 0.2, 1),border-color 90ms cubic-bezier(0.4, 0, 0.2, 1)}.mdc-switch__thumb{box-shadow:0px 3px 1px -2px rgba(0, 0, 0, 0.2),0px 2px 2px 0px rgba(0, 0, 0, 0.14),0px 1px 5px 0px rgba(0,0,0,.12);box-sizing:border-box;width:20px;height:20px;border:10px solid;border-radius:50%;pointer-events:none;z-index:1}.mdc-switch--checked .mdc-switch__track{opacity:.54}.mdc-switch--checked .mdc-switch__thumb-underlay{transform:translateX(16px)}[dir=rtl] .mdc-switch--checked .mdc-switch__thumb-underlay,.mdc-switch--checked .mdc-switch__thumb-underlay[dir=rtl]{transform:translateX(-16px)}.mdc-switch--checked .mdc-switch__native-control{transform:translateX(-16px)}[dir=rtl] .mdc-switch--checked .mdc-switch__native-control,.mdc-switch--checked .mdc-switch__native-control[dir=rtl]{transform:translateX(16px)}.mdc-switch--disabled{opacity:.38;pointer-events:none}.mdc-switch--disabled .mdc-switch__thumb{border-width:1px}.mdc-switch--disabled .mdc-switch__native-control{cursor:default;pointer-events:none}:host{display:inline-flex;outline:none;-webkit-tap-highlight-color:transparent}`;

_decorate([n$2("ha-switch")],function(_initialize,_SwitchBase){class HaSwitch extends _SwitchBase{constructor(...args){super(...args);_initialize(this);}}return {F:HaSwitch,d:[{kind:"field",decorators:[e$1({type:Boolean})],key:"haptic",value(){return false;}},{kind:"method",key:"firstUpdated",value:// Generate a haptic vibration.
// Only set to true if the new value of the switch is applied right away when toggling.
// Do not add haptic when a user is required to press save.
function firstUpdated(){_get(_getPrototypeOf(HaSwitch.prototype),"firstUpdated",this).call(this);this.addEventListener("change",()=>{if(this.haptic){forwardHaptic("light");}});/**
     *               childCard.addEventListener(
                "click",
                (ev: { preventDefault: () => void }) => {
                  ev.preventDefault();
                }
              );
     */}},{kind:"field",static:true,key:"styles",value(){return [styles,r$1`
      :host {
        /* transform: scale(0.9); */
        --mdc-theme-secondary: var(--switch-checked-color);
      }
      .mdc-switch.mdc-switch--checked .mdc-switch__thumb {
        width: 16px;
        height: 16px;
        border: 8px solid;
        background-color: var(--switch-checked-button-color);
        /* border-color: var(--switch-checked-button-color);
        border-color: var(--switch-unchecked-button-color); */
        border-color: #ffffff;
        box-shadow: none;
      }
      .mdc-switch.mdc-switch--checked .mdc-switch__track {
        width: 36px;
        height: 18px;
        border: 0px solid transparent;
        border-radius: 20px;
        background-color: var(--switch-checked-track-color);
        /* border-color: var(--switch-checked-track-color); */
        /* border-color: var(--switch-unchecked-button-color); */
        border-color: #ffffff;
        opacity: 100 !important;
      }

      .mdc-switch:not(.mdc-switch--checked) .mdc-switch__thumb {
        width: 16px;
        height: 16px;
        border: 8px solid;
        background-color: var(--switch-unchecked-button-color);
        /* border-color: var(--switch-unchecked-button-color); */
        border-color: #ffffff;
        box-shadow: none;
      }
      .mdc-switch:not(.mdc-switch--checked) .mdc-switch__track {
        width: 36px;
        height: 18px;
        border: 0px solid transparent;
        border-radius: 20px;
        background-color: var(--switch-unchecked-track-color);
        border-color: var(--switch-unchecked-track-color);
      }

      .mdc-switch__thumb-underlay {
        left: -15px;
        right: initial;
        top: -15px;
        width: 48px;
        height: 48px;
      }

      .mdc-switch--checked .mdc-switch__thumb-underlay {
        transform: translateX(18px);
      }

      .mdc-switch__thumb-underlay > mwc-ripple {
        transform: translate(3px, 3px) scale(0.1);
      }

      .mdc-switch__native-control {
        pointer-events: var(--mdc-switch__pointer_events, "all");
        width: 48px;
        height: 48px;
      }
    `];}}]};},SwitchBase);

/**
Material design:
[Tooltips](https://www.google.com/design/spec/components/tooltips.html)
`<paper-tooltip>` is a label that appears on hover and focus when the user
hovers over an element with the cursor or with the keyboard. It will be centered
to an anchor element specified in the `for` attribute, or, if that doesn't
exist, centered to the parent node containing it.
Example:
    <div style="display:inline-block">
      <button>Click me!</button>
      <paper-tooltip>Tooltip text</paper-tooltip>
    </div>
    <div>
      <button id="btn">Click me!</button>
      <paper-tooltip for="btn">Tooltip text</paper-tooltip>
    </div>
The tooltip can be positioned on the top|bottom|left|right of the anchor using
the `position` attribute. The default position is bottom.
    <paper-tooltip for="btn" position="left">Tooltip text</paper-tooltip>
    <paper-tooltip for="btn" position="top">Tooltip text</paper-tooltip>

### Styling
The following custom properties and mixins are available for styling:
Custom property | Description | Default
----------------|-------------|----------
`--paper-tooltip-background` | The background color of the tooltip | `#616161`
`--paper-tooltip-opacity` | The opacity of the tooltip | `0.9`
`--paper-tooltip-text-color` | The text color of the tooltip | `white`
`--paper-tooltip` | Mixin applied to the tooltip | `{}`
`--paper-tooltip-delay-in` | Delay before tooltip starts to fade in | `500`
`--paper-tooltip-delay-out` | Delay before tooltip starts to fade out | `0`
`--paper-tooltip-duration-in` | Timing for animation when showing tooltip | `500`
`--paper-tooltip-duration-out` | Timing for animation when hiding tooltip | `0`
`--paper-tooltip-animation` | Mixin applied to the tooltip animation | `{}`
@group Paper Elements
@element paper-tooltip
@demo demo/index.html
*/Polymer({_template:html`
    <style>
      :host {
        display: block;
        position: absolute;
        outline: none;
        z-index: 1002;
        -moz-user-select: none;
        -ms-user-select: none;
        -webkit-user-select: none;
        user-select: none;
        cursor: default;
      }

      #tooltip {
        display: block;
        outline: none;
        @apply --paper-font-common-base;
        font-size: 10px;
        line-height: 1;
        background-color: var(--paper-tooltip-background, #616161);
        color: var(--paper-tooltip-text-color, white);
        padding: 8px;
        border-radius: 2px;
        @apply --paper-tooltip;
      }

      @keyframes keyFrameScaleUp {
        0% {
          transform: scale(0.0);
        }
        100% {
          transform: scale(1.0);
        }
      }

      @keyframes keyFrameScaleDown {
        0% {
          transform: scale(1.0);
        }
        100% {
          transform: scale(0.0);
        }
      }

      @keyframes keyFrameFadeInOpacity {
        0% {
          opacity: 0;
        }
        100% {
          opacity: var(--paper-tooltip-opacity, 0.9);
        }
      }

      @keyframes keyFrameFadeOutOpacity {
        0% {
          opacity: var(--paper-tooltip-opacity, 0.9);
        }
        100% {
          opacity: 0;
        }
      }

      @keyframes keyFrameSlideDownIn {
        0% {
          transform: translateY(-2000px);
          opacity: 0;
        }
        10% {
          opacity: 0.2;
        }
        100% {
          transform: translateY(0);
          opacity: var(--paper-tooltip-opacity, 0.9);
        }
      }

      @keyframes keyFrameSlideDownOut {
        0% {
          transform: translateY(0);
          opacity: var(--paper-tooltip-opacity, 0.9);
        }
        10% {
          opacity: 0.2;
        }
        100% {
          transform: translateY(-2000px);
          opacity: 0;
        }
      }

      .fade-in-animation {
        opacity: 0;
        animation-delay: var(--paper-tooltip-delay-in, 500ms);
        animation-name: keyFrameFadeInOpacity;
        animation-iteration-count: 1;
        animation-timing-function: ease-in;
        animation-duration: var(--paper-tooltip-duration-in, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .fade-out-animation {
        opacity: var(--paper-tooltip-opacity, 0.9);
        animation-delay: var(--paper-tooltip-delay-out, 0ms);
        animation-name: keyFrameFadeOutOpacity;
        animation-iteration-count: 1;
        animation-timing-function: ease-in;
        animation-duration: var(--paper-tooltip-duration-out, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .scale-up-animation {
        transform: scale(0);
        opacity: var(--paper-tooltip-opacity, 0.9);
        animation-delay: var(--paper-tooltip-delay-in, 500ms);
        animation-name: keyFrameScaleUp;
        animation-iteration-count: 1;
        animation-timing-function: ease-in;
        animation-duration: var(--paper-tooltip-duration-in, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .scale-down-animation {
        transform: scale(1);
        opacity: var(--paper-tooltip-opacity, 0.9);
        animation-delay: var(--paper-tooltip-delay-out, 500ms);
        animation-name: keyFrameScaleDown;
        animation-iteration-count: 1;
        animation-timing-function: ease-in;
        animation-duration: var(--paper-tooltip-duration-out, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .slide-down-animation {
        transform: translateY(-2000px);
        opacity: 0;
        animation-delay: var(--paper-tooltip-delay-out, 500ms);
        animation-name: keyFrameSlideDownIn;
        animation-iteration-count: 1;
        animation-timing-function: cubic-bezier(0.0, 0.0, 0.2, 1);
        animation-duration: var(--paper-tooltip-duration-out, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .slide-down-animation-out {
        transform: translateY(0);
        opacity: var(--paper-tooltip-opacity, 0.9);
        animation-delay: var(--paper-tooltip-delay-out, 500ms);
        animation-name: keyFrameSlideDownOut;
        animation-iteration-count: 1;
        animation-timing-function: cubic-bezier(0.4, 0.0, 1, 1);
        animation-duration: var(--paper-tooltip-duration-out, 500ms);
        animation-fill-mode: forwards;
        @apply --paper-tooltip-animation;
      }

      .cancel-animation {
        animation-delay: -30s !important;
      }

      /* Thanks IE 10. */

      .hidden {
        display: none !important;
      }
    </style>

    <div id="tooltip" class="hidden">
      <slot></slot>
    </div>
`,is:'paper-tooltip',hostAttributes:{role:'tooltip',tabindex:-1},properties:{/**
     * The id of the element that the tooltip is anchored to. This element
     * must be a sibling of the tooltip. If this property is not set,
     * then the tooltip will be centered to the parent node containing it.
     */for:{type:String,observer:'_findTarget'},/**
     * Set this to true if you want to manually control when the tooltip
     * is shown or hidden.
     */manualMode:{type:Boolean,value:false,observer:'_manualModeChanged'},/**
     * Positions the tooltip to the top, right, bottom, left of its content.
     */position:{type:String,value:'bottom'},/**
     * If true, no parts of the tooltip will ever be shown offscreen.
     */fitToVisibleBounds:{type:Boolean,value:false},/**
     * The spacing between the top of the tooltip and the element it is
     * anchored to.
     */offset:{type:Number,value:14},/**
     * This property is deprecated, but left over so that it doesn't
     * break exiting code. Please use `offset` instead. If both `offset` and
     * `marginTop` are provided, `marginTop` will be ignored.
     * @deprecated since version 1.0.3
     */marginTop:{type:Number,value:14},/**
     * The delay that will be applied before the `entry` animation is
     * played when showing the tooltip.
     */animationDelay:{type:Number,value:500,observer:'_delayChange'},/**
     * The animation that will be played on entry.  This replaces the
     * deprecated animationConfig.  Entries here will override the
     * animationConfig settings.  You can enter your own animation
     * by setting it to the css class name.
     */animationEntry:{type:String,value:''},/**
     * The animation that will be played on exit.  This replaces the
     * deprecated animationConfig.  Entries here will override the
     * animationConfig settings.  You can enter your own animation
     * by setting it to the css class name.
     */animationExit:{type:String,value:''},/**
     * This property is deprecated.  Use --paper-tooltip-animation to change the
     * animation. The entry and exit animations that will be played when showing
     * and hiding the tooltip. If you want to override this, you must ensure
     * that your animationConfig has the exact format below.
     * @deprecated since version
     *
     * The entry and exit animations that will be played when showing and
     * hiding the tooltip. If you want to override this, you must ensure
     * that your animationConfig has the exact format below.
     */animationConfig:{type:Object,value:function(){return {'entry':[{name:'fade-in-animation',node:this,timing:{delay:0}}],'exit':[{name:'fade-out-animation',node:this}]};}},_showing:{type:Boolean,value:false}},listeners:{'webkitAnimationEnd':'_onAnimationEnd'},/**
   * Returns the target element that this tooltip is anchored to. It is
   * either the element given by the `for` attribute, or the immediate parent
   * of the tooltip.
   *
   * @type {Node}
   */get target(){var parentNode=dom(this).parentNode;// If the parentNode is a document fragment, then we need to use the host.
var ownerRoot=dom(this).getOwnerRoot();var target;if(this.for){target=dom(ownerRoot).querySelector('#'+this.for);}else {target=parentNode.nodeType==Node.DOCUMENT_FRAGMENT_NODE?ownerRoot.host:parentNode;}return target;},/**
   * @return {void}
   */attached:function(){this._findTarget();},/**
   * @return {void}
   */detached:function(){if(!this.manualMode)this._removeListeners();},/**
   * Replaces Neon-Animation playAnimation - just calls show and hide.
   * @deprecated Use show and hide instead.
   * @param {string} type Either `entry` or `exit`
   */playAnimation:function(type){if(type==='entry'){this.show();}else if(type==='exit'){this.hide();}},/**
   * Cancels the animation and either fully shows or fully hides tooltip
   */cancelAnimation:function(){// Short-cut and cancel all animations and hide
this.$.tooltip.classList.add('cancel-animation');},/**
   * Shows the tooltip programatically
   * @return {void}
   */show:function(){// If the tooltip is already showing, there's nothing to do.
if(this._showing)return;if(dom(this).textContent.trim()===''){// Check if effective children are also empty
var allChildrenEmpty=true;var effectiveChildren=dom(this).getEffectiveChildNodes();for(var i=0;i<effectiveChildren.length;i++){if(effectiveChildren[i].textContent.trim()!==''){allChildrenEmpty=false;break;}}if(allChildrenEmpty){return;}}this._showing=true;this.$.tooltip.classList.remove('hidden');this.$.tooltip.classList.remove('cancel-animation');this.$.tooltip.classList.remove(this._getAnimationType('exit'));this.updatePosition();this._animationPlaying=true;this.$.tooltip.classList.add(this._getAnimationType('entry'));},/**
   * Hides the tooltip programatically
   * @return {void}
   */hide:function(){// If the tooltip is already hidden, there's nothing to do.
if(!this._showing){return;}// If the entry animation is still playing, don't try to play the exit
// animation since this will reset the opacity to 1. Just end the animation.
if(this._animationPlaying){this._showing=false;this._cancelAnimation();return;}else {// Play Exit Animation
this._onAnimationFinish();}this._showing=false;this._animationPlaying=true;},/**
   * @return {void}
   */updatePosition:function(){if(!this._target||!this.offsetParent)return;var offset=this.offset;// If a marginTop has been provided by the user (pre 1.0.3), use it.
if(this.marginTop!=14&&this.offset==14)offset=this.marginTop;var parentRect=this.offsetParent.getBoundingClientRect();var targetRect=this._target.getBoundingClientRect();var thisRect=this.getBoundingClientRect();var horizontalCenterOffset=(targetRect.width-thisRect.width)/2;var verticalCenterOffset=(targetRect.height-thisRect.height)/2;var targetLeft=targetRect.left-parentRect.left;var targetTop=targetRect.top-parentRect.top;var tooltipLeft,tooltipTop;switch(this.position){case'top':tooltipLeft=targetLeft+horizontalCenterOffset;tooltipTop=targetTop-thisRect.height-offset;break;case'bottom':tooltipLeft=targetLeft+horizontalCenterOffset;tooltipTop=targetTop+targetRect.height+offset;break;case'left':tooltipLeft=targetLeft-thisRect.width-offset;tooltipTop=targetTop+verticalCenterOffset;break;case'right':tooltipLeft=targetLeft+targetRect.width+offset;tooltipTop=targetTop+verticalCenterOffset;break;}// TODO(noms): This should use IronFitBehavior if possible.
if(this.fitToVisibleBounds){// Clip the left/right side
if(parentRect.left+tooltipLeft+thisRect.width>window.innerWidth){this.style.right='0px';this.style.left='auto';}else {this.style.left=Math.max(0,tooltipLeft)+'px';this.style.right='auto';}// Clip the top/bottom side.
if(parentRect.top+tooltipTop+thisRect.height>window.innerHeight){this.style.bottom=parentRect.height-targetTop+offset+'px';this.style.top='auto';}else {this.style.top=Math.max(-parentRect.top,tooltipTop)+'px';this.style.bottom='auto';}}else {this.style.left=tooltipLeft+'px';this.style.top=tooltipTop+'px';}},_addListeners:function(){if(this._target){this.listen(this._target,'mouseenter','show');this.listen(this._target,'focus','show');this.listen(this._target,'mouseleave','hide');this.listen(this._target,'blur','hide');this.listen(this._target,'tap','hide');}this.listen(this.$.tooltip,'animationend','_onAnimationEnd');this.listen(this,'mouseenter','hide');},_findTarget:function(){if(!this.manualMode)this._removeListeners();this._target=this.target;if(!this.manualMode)this._addListeners();},_delayChange:function(newValue){// Only Update delay if different value set
if(newValue!==500){this.updateStyles({'--paper-tooltip-delay-in':newValue+'ms'});}},_manualModeChanged:function(){if(this.manualMode)this._removeListeners();else this._addListeners();},_cancelAnimation:function(){// Short-cut and cancel all animations and hide
this.$.tooltip.classList.remove(this._getAnimationType('entry'));this.$.tooltip.classList.remove(this._getAnimationType('exit'));this.$.tooltip.classList.remove('cancel-animation');this.$.tooltip.classList.add('hidden');},_onAnimationFinish:function(){if(this._showing){this.$.tooltip.classList.remove(this._getAnimationType('entry'));this.$.tooltip.classList.remove('cancel-animation');this.$.tooltip.classList.add(this._getAnimationType('exit'));}},_onAnimationEnd:function(){// If no longer showing add class hidden to completely hide tooltip
this._animationPlaying=false;if(!this._showing){this.$.tooltip.classList.remove(this._getAnimationType('exit'));this.$.tooltip.classList.add('hidden');}},_getAnimationType:function(type){// These properties have priority over animationConfig values
if(type==='entry'&&this.animationEntry!==''){return this.animationEntry;}if(type==='exit'&&this.animationExit!==''){return this.animationExit;}// If no results then return the legacy value from animationConfig
if(this.animationConfig[type]&&typeof this.animationConfig[type][0].name==='string'){// Checking Timing and Update if necessary - Legacy for animationConfig
if(this.animationConfig[type][0].timing&&this.animationConfig[type][0].timing.delay&&this.animationConfig[type][0].timing.delay!==0){var timingDelay=this.animationConfig[type][0].timing.delay;// Has Timing Change - Update CSS
if(type==='entry'){this.updateStyles({'--paper-tooltip-delay-in':timingDelay+'ms'});}else if(type==='exit'){this.updateStyles({'--paper-tooltip-delay-out':timingDelay+'ms'});}}return this.animationConfig[type][0].name;}},_removeListeners:function(){if(this._target){this.unlisten(this._target,'mouseenter','show');this.unlisten(this._target,'focus','show');this.unlisten(this._target,'mouseleave','hide');this.unlisten(this._target,'blur','hide');this.unlisten(this._target,'tap','hide');}this.unlisten(this.$.tooltip,'animationend','_onAnimationEnd');this.unlisten(this,'mouseenter','hide');}});

const capitalizeFirstLetter=str=>str.charAt(0).toUpperCase()+str.slice(1);

const computeActiveState=stateObj=>{const domain=stateObj.entity_id.split(".")[0];let state=stateObj.state;if(domain==="climate"){state=stateObj.attributes.hvac_action;}return state;};

const iconColorCSS=r$1`
  ha-state-icon[data-domain="alert"][data-state="on"],
  ha-state-icon[data-domain="automation"][data-state="on"],
  ha-state-icon[data-domain="binary_sensor"][data-state="on"],
  ha-state-icon[data-domain="calendar"][data-state="on"],
  ha-state-icon[data-domain="camera"][data-state="streaming"],
  ha-state-icon[data-domain="cover"][data-state="open"],
  ha-state-icon[data-domain="fan"][data-state="on"],
  ha-state-icon[data-domain="humidifier"][data-state="on"],
  ha-state-icon[data-domain="light"][data-state="on"],
  ha-state-icon[data-domain="input_boolean"][data-state="on"],
  ha-state-icon[data-domain="lock"][data-state="unlocked"],
  ha-state-icon[data-domain="media_player"][data-state="on"],
  ha-state-icon[data-domain="media_player"][data-state="paused"],
  ha-state-icon[data-domain="media_player"][data-state="playing"],
  ha-state-icon[data-domain="remote"][data-state="on"],
  ha-state-icon[data-domain="script"][data-state="on"],
  ha-state-icon[data-domain="sun"][data-state="above_horizon"],
  ha-state-icon[data-domain="switch"][data-state="on"],
  ha-state-icon[data-domain="timer"][data-state="active"],
  ha-state-icon[data-domain="vacuum"][data-state="cleaning"],
  ha-state-icon[data-domain="group"][data-state="on"],
  ha-state-icon[data-domain="group"][data-state="home"],
  ha-state-icon[data-domain="group"][data-state="open"],
  ha-state-icon[data-domain="group"][data-state="locked"],
  ha-state-icon[data-domain="group"][data-state="problem"] {
    color: var(--paper-item-icon-active-color, #fdd835);
  }

  ha-state-icon[data-domain="climate"][data-state="cooling"] {
    color: var(--cool-color, var(--state-climate-cool-color));
  }

  ha-state-icon[data-domain="climate"][data-state="heating"] {
    color: var(--heat-color, var(--state-climate-heat-color));
  }

  ha-state-icon[data-domain="climate"][data-state="drying"] {
    color: var(--dry-color, var(--state-climate-dry-color));
  }

  ha-state-icon[data-domain="alarm_control_panel"] {
    color: var(--alarm-color-armed, var(--label-badge-red));
  }
  ha-state-icon[data-domain="alarm_control_panel"][data-state="disarmed"] {
    color: var(--alarm-color-disarmed, var(--label-badge-green));
  }
  ha-state-icon[data-domain="alarm_control_panel"][data-state="pending"],
  ha-state-icon[data-domain="alarm_control_panel"][data-state="arming"] {
    color: var(--alarm-color-pending, var(--label-badge-yellow));
    animation: pulse 1s infinite;
  }
  ha-state-icon[data-domain="alarm_control_panel"][data-state="triggered"] {
    color: var(--alarm-color-triggered, var(--label-badge-red));
    animation: pulse 1s infinite;
  }

  @keyframes pulse {
    0% {
      opacity: 1;
    }
    50% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

  ha-state-icon[data-domain="plant"][data-state="problem"],
  ha-state-icon[data-domain="zwave"][data-state="dead"] {
    color: var(--state-icon-error-color);
  }

  /* Color the icon if unavailable */
  ha-state-icon[data-state="unavailable"] {
    color: var(--state-unavailable-color);
  }
`;

const alarmPanelIcon=state=>{switch(state){case"armed_away":return mdiShieldLock;case"armed_vacation":return mdiShieldAirplane;case"armed_home":return mdiShieldHome;case"armed_night":return mdiShieldMoon;case"armed_custom_bypass":return mdiSecurity;case"pending":return mdiShieldOutline;case"triggered":return mdiBellRing;case"disarmed":return mdiShieldOff;default:return mdiShield;}};

/** Return an icon representing a binary sensor state. */const binarySensorIcon=(state,stateObj)=>{const is_off=state==="off";switch(stateObj===null||stateObj===void 0?void 0:stateObj.attributes.device_class){case"battery":return is_off?mdiBattery:mdiBatteryOutline;case"battery_charging":return is_off?mdiBattery:mdiBatteryCharging;case"cold":return is_off?mdiThermometer:mdiSnowflake;case"connectivity":return is_off?mdiCloseNetworkOutline:mdiCheckNetworkOutline;case"door":return is_off?mdiDoorClosed:mdiDoorOpen;case"garage_door":return is_off?mdiGarage:mdiGarageOpen;case"power":return is_off?mdiLightbulb:mdiLightbulb;case"gas":case"problem":case"safety":case"tamper":return is_off?mdiCheckCircle:mdiAlertCircle;case"smoke":return is_off?mdiCheckCircle:mdiSmoke;case"heat":return is_off?mdiThermometer:mdiFire;case"light":return is_off?mdiBrightness5:mdiBrightness7;case"lock":return is_off?mdiLock:mdiLockOpen;case"moisture":return is_off?mdiWaterOff:mdiWater;case"motion":return is_off?mdiMotionSensorOff:mdiMotionSensor;case"occupancy":return is_off?mdiHomeOutline:mdiHome;case"opening":return is_off?mdiSquare:mdiSquareOutline;case"plug":return is_off?mdiPowerPlugOff:mdiPowerPlug;case"presence":return is_off?mdiHomeOutline:mdiHome;case"running":return is_off?mdiStop:mdiPlay;case"sound":return is_off?mdiMusicNoteOff:mdiMusicNote;case"update":return is_off?mdiPackage:mdiPackageUp;case"vibration":return is_off?mdiCropPortrait:mdiVibrate;case"window":return is_off?mdiWindowClosed:mdiWindowOpen;default:return is_off?mdiRadioboxBlank:mdiCheckboxMarkedCircle;}};

const coverIcon=(state,stateObj)=>{const open=state!=="closed";switch(stateObj===null||stateObj===void 0?void 0:stateObj.attributes.device_class){case"garage":switch(state){case"opening":return mdiArrowUpBox;case"closing":return mdiArrowDownBox;case"closed":return mdiGarage;default:return mdiGarageOpen;}case"gate":switch(state){case"opening":case"closing":return mdiGateArrowRight;case"closed":return mdiGate;default:return mdiGateOpen;}case"door":return open?mdiDoorOpen:mdiDoorClosed;case"damper":return open?mdiCircle:mdiCircleSlice8;case"shutter":switch(state){case"opening":return mdiArrowUpBox;case"closing":return mdiArrowDownBox;case"closed":return mdiWindowShutter;default:return mdiWindowShutterOpen;}case"curtain":switch(state){case"opening":return mdiArrowSplitVertical;case"closing":return mdiArrowCollapseHorizontal;case"closed":return mdiCurtainsClosed;default:return mdiCurtains;}case"blind":case"shade":switch(state){case"opening":return mdiArrowUpBox;case"closing":return mdiArrowDownBox;case"closed":return mdiBlinds;default:return mdiBlindsOpen;}case"window":switch(state){case"opening":return mdiArrowUpBox;case"closing":return mdiArrowDownBox;case"closed":return mdiWindowClosed;default:return mdiWindowOpen;}}switch(state){case"opening":return mdiArrowUpBox;case"closing":return mdiArrowDownBox;case"closed":return mdiWindowClosed;default:return mdiWindowOpen;}};const computeOpenIcon=stateObj=>{switch(stateObj.attributes.device_class){case"awning":case"door":case"gate":case"curtain":return mdiArrowExpandHorizontal;default:return mdiArrowUp;}};const computeCloseIcon=stateObj=>{switch(stateObj.attributes.device_class){case"awning":case"door":case"gate":case"curtain":return mdiArrowCollapseHorizontal;default:return mdiArrowDown;}};

const SENSOR_DEVICE_CLASS_BATTERY="battery";const SENSOR_DEVICE_CLASS_TIMESTAMP="timestamp";

const BATTERY_ICONS={10:mdiBattery10,20:mdiBattery20,30:mdiBattery30,40:mdiBattery40,50:mdiBattery50,60:mdiBattery60,70:mdiBattery70,80:mdiBattery80,90:mdiBattery90,100:mdiBattery};const BATTERY_CHARGING_ICONS={10:mdiBatteryCharging10,20:mdiBatteryCharging20,30:mdiBatteryCharging30,40:mdiBatteryCharging40,50:mdiBatteryCharging50,60:mdiBatteryCharging60,70:mdiBatteryCharging70,80:mdiBatteryCharging80,90:mdiBatteryCharging90,100:mdiBatteryCharging};const batteryStateIcon=(batteryState,batteryChargingState)=>{const battery=batteryState.state;const batteryCharging=batteryChargingState&&batteryChargingState.state==="on";return batteryIcon(battery,batteryCharging);};const batteryIcon=(batteryState,batteryCharging)=>{const batteryValue=Number(batteryState);if(isNaN(batteryValue)){if(batteryState==="off"){return mdiBattery;}if(batteryState==="on"){return mdiBatteryAlert;}return mdiBatteryUnknown;}const batteryRound=Math.round(batteryValue/10)*10;if(batteryCharging&&batteryValue>=10){return BATTERY_CHARGING_ICONS[batteryRound];}if(batteryCharging){return mdiBatteryChargingOutline;}if(batteryValue<=5){return mdiBatteryAlertVariantOutline;}return BATTERY_ICONS[batteryRound];};

const sensorIcon=stateObj=>{const dclass=stateObj===null||stateObj===void 0?void 0:stateObj.attributes.device_class;if(dclass&&dclass in FIXED_DEVICE_CLASS_ICONS){return FIXED_DEVICE_CLASS_ICONS[dclass];}if(dclass===SENSOR_DEVICE_CLASS_BATTERY){return stateObj?batteryStateIcon(stateObj):mdiBattery;}const unit=stateObj===null||stateObj===void 0?void 0:stateObj.attributes.unit_of_measurement;if(unit===UNIT_C||unit===UNIT_F){return mdiThermometer;}return undefined;};

const domainIcon=(domain,stateObj,state)=>{const compareState=state!==undefined?state:stateObj===null||stateObj===void 0?void 0:stateObj.state;switch(domain){case"alarm_control_panel":return alarmPanelIcon(compareState);case"binary_sensor":return binarySensorIcon(compareState,stateObj);case"button":switch(stateObj===null||stateObj===void 0?void 0:stateObj.attributes.device_class){case"restart":return mdiRestart;case"update":return mdiPackageUp;default:return mdiGestureTapButton;}case"cover":return coverIcon(compareState,stateObj);case"device_tracker":if((stateObj===null||stateObj===void 0?void 0:stateObj.attributes.source_type)==="router"){return compareState==="home"?mdiLanConnect:mdiLanDisconnect;}if(["bluetooth","bluetooth_le"].includes(stateObj===null||stateObj===void 0?void 0:stateObj.attributes.source_type)){return compareState==="home"?mdiBluetoothConnect:mdiBluetooth;}return compareState==="not_home"?mdiAccountArrowRight:mdiAccount;case"humidifier":return state&&state==="off"?mdiAirHumidifierOff:mdiAirHumidifier;case"input_boolean":return compareState==="on"?mdiCheckCircleOutline:mdiCloseCircleOutline;case"lock":switch(compareState){case"unlocked":return mdiLockOpen;case"jammed":return mdiLockAlert;case"locking":case"unlocking":return mdiLockClock;default:return mdiLock;}case"media_player":return compareState==="playing"?mdiCastConnected:mdiCast;case"switch":switch(stateObj===null||stateObj===void 0?void 0:stateObj.attributes.device_class){case"outlet":return compareState==="on"?mdiPowerPlug:mdiPowerPlugOff;case"switch":return compareState==="on"?mdiToggleSwitch:mdiToggleSwitchOff;default:return mdiFlash;}case"zwave":switch(compareState){case"dead":return mdiEmoticonDead;case"sleeping":return mdiSleep;case"initializing":return mdiTimerSand;default:return mdiZWave;}case"sensor":{const icon=sensorIcon(stateObj);if(icon){return icon;}break;}case"input_datetime":if(!(stateObj!==null&&stateObj!==void 0&&stateObj.attributes.has_date)){return mdiClock;}if(!stateObj.attributes.has_time){return mdiCalendar;}break;case"sun":return (stateObj===null||stateObj===void 0?void 0:stateObj.state)==="above_horizon"?FIXED_DOMAIN_ICONS[domain]:mdiWeatherNight;}if(domain in FIXED_DOMAIN_ICONS){return FIXED_DOMAIN_ICONS[domain];}// eslint-disable-next-line
console.warn(`Unable to find icon for domain ${domain}`);return DEFAULT_DOMAIN_ICON;};

const stateIconPath=state=>{if(!state){return DEFAULT_DOMAIN_ICON;}return domainIcon(computeDomain(state.entity_id),state);};

_decorate([n$2("ha-state-icon")],function(_initialize,_LitElement){class HaStateIcon extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaStateIcon,d:[{kind:"field",decorators:[e$1({attribute:false})],key:"state",value:void 0},{kind:"field",decorators:[e$1()],key:"icon",value:void 0},{kind:"method",key:"render",value:function render(){var _this$state;if(this.icon||(_this$state=this.state)!==null&&_this$state!==void 0&&_this$state.attributes.icon){var _this$state2;return $`<ha-icon
        .icon=${this.icon||((_this$state2=this.state)===null||_this$state2===void 0?void 0:_this$state2.attributes.icon)}
      ></ha-icon>`;}return $`<ha-svg-icon .path=${stateIconPath(this.state)}></ha-svg-icon>`;}}]};},s$1);

let StateBadge=_decorate(null,function(_initialize,_LitElement){class StateBadge extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:StateBadge,d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[e$1()],key:"stateObj",value:void 0},{kind:"field",decorators:[e$1()],key:"overrideIcon",value:void 0},{kind:"field",decorators:[e$1()],key:"overrideImage",value:void 0},{kind:"field",decorators:[e$1({type:Boolean})],key:"stateColor",value:void 0},{kind:"field",decorators:[e$1({type:Boolean,reflect:true,attribute:"icon"})],key:"_showIcon",value(){return true;}},{kind:"field",decorators:[t()],key:"_iconStyle",value(){return {};}},{kind:"method",key:"render",value:function render(){const stateObj=this.stateObj;// We either need a `stateObj` or one override
if(!stateObj&&!this.overrideIcon&&!this.overrideImage){return $`<div class="missing">
        <ha-svg-icon .path=${mdiAlert}></ha-svg-icon>
      </div>`;}if(!this._showIcon){return $``;}const domain=stateObj?computeStateDomain(stateObj):undefined;return $`
      <ha-state-icon
        style=${i$2(this._iconStyle)}
        data-domain=${l$1(this.stateColor||domain==="light"&&this.stateColor!==false?domain:undefined)}
        data-state=${stateObj?computeActiveState(stateObj):""}
        .icon=${this.overrideIcon}
        .state=${stateObj}
      ></ha-state-icon>
    `;}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){_get(_getPrototypeOf(StateBadge.prototype),"willUpdate",this).call(this,changedProps);if(!changedProps.has("stateObj")&&!changedProps.has("overrideImage")&&!changedProps.has("overrideIcon")){return;}const stateObj=this.stateObj;const iconStyle={};const hostStyle={backgroundImage:""};this._showIcon=true;if(stateObj&&this.overrideImage===undefined){// hide icon if we have entity picture
if((stateObj.attributes.entity_picture_local||stateObj.attributes.entity_picture)&&!this.overrideIcon){let imageUrl=stateObj.attributes.entity_picture_local||stateObj.attributes.entity_picture;if(this.hass){imageUrl=this.hass.hassUrl(imageUrl);}hostStyle.backgroundImage=`url(${imageUrl})`;this._showIcon=false;}else if(stateObj.state==="on"){const domain=stateObj?computeStateDomain(stateObj):undefined;if(domain==="light"){iconStyle.color="var(--state-light-active-color, #ffbd4b)";}else {iconStyle.color="var(--state-icon-active-color)";}if(this.stateColor!==false&&stateObj.attributes.rgb_color){iconStyle.color=`rgb(${stateObj.attributes.rgb_color.join(",")})`;}if(stateObj.attributes.brightness&&this.stateColor!==false){const brightness=stateObj.attributes.brightness;if(typeof brightness!=="number"){const errorMessage=`Type error: state-badge expected number, but type of ${stateObj.entity_id}.attributes.brightness is ${typeof brightness} (${brightness})`;// eslint-disable-next-line
console.warn(errorMessage);}// lowest brightness will be around 50% (that's pretty dark)
iconStyle.filter=`brightness(${(brightness+245)/5}%)`;}}}else if(this.overrideImage){let imageUrl=this.overrideImage;if(this.hass){imageUrl=this.hass.hassUrl(imageUrl);}hostStyle.backgroundImage=`url(${imageUrl})`;this._showIcon=false;}this._iconStyle=iconStyle;Object.assign(this.style,hostStyle);}},{kind:"get",static:true,key:"styles",value:function styles(){return [iconColorCSS,r$1`
        :host {
          position: relative;
          display: inline-block;
          width: 24px;
          color: var(--paper-item-icon-color, #44739e);
          border-radius: 50%;
          height: 24px;
          text-align: center;
          background-size: cover;
          line-height: 22px;
          vertical-align: middle;
          box-sizing: border-box;
        }
        :host(:focus) {
          outline: none;
        }
        :host(:not([icon]):focus) {
          border: 2px solid var(--divider-color);
        }
        :host([icon]:focus) {
          background: var(--divider-color);
        }
        ha-state-icon {
          transition: color 0.3s ease-in-out, filter 0.3s ease-in-out;
          --mdc-icon-size: 100%;
          width: 40px;
        }
        ha-svg-icon {
          width: 40px;
          height: auto;
        }
        .missing {
          color: #fce588;
        }
      `];}}]};},s$1);customElements.define("state-badge",StateBadge);

const SUPPORT_PAUSE=1;const SUPPORT_SEEK=2;const SUPPORT_VOLUME_SET=4;const SUPPORT_VOLUME_MUTE=8;const SUPPORT_PREVIOUS_TRACK=16;const SUPPORT_NEXT_TRACK=32;const SUPPORT_TURN_ON=128;const SUPPORT_TURN_OFF=256;const SUPPORT_PLAY_MEDIA=512;const SUPPORT_VOLUME_BUTTONS=1024;const SUPPORT_SELECT_SOURCE=2048;const SUPPORT_STOP=4096;const SUPPORT_PLAY=16384;const SUPPORT_SELECT_SOUND_MODE=65536;const SUPPORT_BROWSE_MEDIA=131072;const BROWSER_PLAYER="browser";const MediaClassBrowserSettings={album:{icon:mdiAlbum,layout:"grid"},app:{icon:mdiApplication,layout:"grid"},artist:{icon:mdiAccountMusic,layout:"grid",show_list_images:true},channel:{icon:mdiTelevisionClassic,thumbnail_ratio:"portrait",layout:"grid"},composer:{icon:mdiAccountMusicOutline,layout:"grid",show_list_images:true},contributing_artist:{icon:mdiAccountMusic,layout:"grid",show_list_images:true},directory:{icon:mdiFolder,layout:"grid",show_list_images:true},episode:{icon:mdiTelevisionClassic,layout:"grid",thumbnail_ratio:"portrait"},game:{icon:mdiGamepadVariant,layout:"grid",thumbnail_ratio:"portrait"},genre:{icon:mdiDramaMasks,layout:"grid",show_list_images:true},image:{icon:mdiImage,layout:"grid"},movie:{icon:mdiMovie,thumbnail_ratio:"portrait",layout:"grid"},music:{icon:mdiMusic},playlist:{icon:mdiPlaylistMusic,layout:"grid",show_list_images:true},podcast:{icon:mdiPodcast,layout:"grid"},season:{icon:mdiTelevisionClassic,layout:"grid",thumbnail_ratio:"portrait"},track:{icon:mdiFileMusic},tv_show:{icon:mdiTelevisionClassic,layout:"grid",thumbnail_ratio:"portrait"},url:{icon:mdiWeb},video:{icon:mdiVideo,layout:"grid"}};const browseMediaPlayer=(hass,entityId,mediaContentId,mediaContentType)=>hass.callWS({type:"media_player/browse_media",entity_id:entityId,media_content_id:mediaContentId,media_content_type:mediaContentType});const getCurrentProgress=stateObj=>{let progress=stateObj.attributes.media_position;if(stateObj.state!=="playing"){return progress;}progress+=(Date.now()-new Date(stateObj.attributes.media_position_updated_at).getTime())/1000.0;return progress;};const computeMediaDescription=stateObj=>{let secondaryTitle;switch(stateObj.attributes.media_content_type){case"music":case"image":secondaryTitle=stateObj.attributes.media_artist;break;case"playlist":secondaryTitle=stateObj.attributes.media_playlist;break;case"tvshow":secondaryTitle=stateObj.attributes.media_series_title;if(stateObj.attributes.media_season){secondaryTitle+=" S"+stateObj.attributes.media_season;if(stateObj.attributes.media_episode){secondaryTitle+="E"+stateObj.attributes.media_episode;}}break;default:secondaryTitle=stateObj.attributes.app_name||"";}return secondaryTitle;};const computeMediaControls=stateObj=>{if(!stateObj){return undefined;}const state=stateObj.state;if(UNAVAILABLE_STATES.includes(state)){return undefined;}if(state==="off"){return supportsFeature(stateObj,SUPPORT_TURN_ON)?[{icon:mdiPower,action:"turn_on"}]:undefined;}const buttons=[];if(supportsFeature(stateObj,SUPPORT_TURN_OFF)){buttons.push({icon:mdiPower,action:"turn_off"});}const assumedState=stateObj.attributes.assumed_state===true;if((state==="playing"||state==="paused"||assumedState)&&supportsFeature(stateObj,SUPPORT_PREVIOUS_TRACK)){buttons.push({icon:mdiSkipPrevious,action:"media_previous_track"});}if(!assumedState&&(state==="playing"&&(supportsFeature(stateObj,SUPPORT_PAUSE)||supportsFeature(stateObj,SUPPORT_STOP))||(state==="paused"||state==="idle")&&supportsFeature(stateObj,SUPPORT_PLAY)||state==="on"&&(supportsFeature(stateObj,SUPPORT_PLAY)||supportsFeature(stateObj,SUPPORT_PAUSE)))){buttons.push({icon:state==="on"?mdiPlayPause:state!=="playing"?mdiPlay:supportsFeature(stateObj,SUPPORT_PAUSE)?mdiPause:mdiStop,action:state!=="playing"?"media_play":supportsFeature(stateObj,SUPPORT_PAUSE)?"media_pause":"media_stop"});}if(assumedState&&supportsFeature(stateObj,SUPPORT_PLAY)){buttons.push({icon:mdiPlay,action:"media_play"});}if(assumedState&&supportsFeature(stateObj,SUPPORT_PAUSE)){buttons.push({icon:mdiPause,action:"media_pause"});}if(assumedState&&supportsFeature(stateObj,SUPPORT_STOP)){buttons.push({icon:mdiStop,action:"media_stop"});}if((state==="playing"||state==="paused"||assumedState)&&supportsFeature(stateObj,SUPPORT_NEXT_TRACK)){buttons.push({icon:mdiSkipNext,action:"media_next_track"});}return buttons.length>0?buttons:undefined;};const cleanupMediaTitle=title=>{if(!title){return undefined;}const index=title.indexOf("?authSig=");return index>0?title.slice(0,index):title;};

/**
 * A `StructFailure` represents a single specific failure in validation.
 */ /**
 * `StructError` objects are thrown (or returned) when validation fails.
 *
 * Validation logic is design to exit early for maximum performance. The error
 * represents the first error encountered during validation. For more detail,
 * the `error.failures` property is a generator function that can be run to
 * continue validation and receive all the failures in the data.
 */class StructError extends TypeError{constructor(failure,failures){let cached;const{message,...rest}=failure;const{path}=failure;const msg=path.length===0?message:"At path: "+path.join('.')+" -- "+message;super(msg);this.value=void 0;this.key=void 0;this.type=void 0;this.refinement=void 0;this.path=void 0;this.branch=void 0;this.failures=void 0;Object.assign(this,rest);this.name=this.constructor.name;this.failures=()=>{var _cached;return (_cached=cached)!=null?_cached:cached=[failure,...failures()];};}}/**
 * Check if a value is an iterator.
 */function isIterable(x){return isObject(x)&&typeof x[Symbol.iterator]==='function';}/**
 * Check if a value is a plain object.
 */function isObject(x){return typeof x==='object'&&x!=null;}/**
 * Return a value as a printable string.
 */function print(value){return typeof value==='string'?JSON.stringify(value):""+value;}/**
 * Shifts (removes and returns) the first value from the `input` iterator.
 * Like `Array.prototype.shift()` but for an `Iterator`.
 */function shiftIterator(input){const{done,value}=input.next();return done?undefined:value;}/**
 * Convert a single validation result to a failure.
 */function toFailure(result,context,struct,value){if(result===true){return;}else if(result===false){result={};}else if(typeof result==='string'){result={message:result};}const{path,branch}=context;const{type}=struct;const{refinement,message="Expected a value of type `"+type+"`"+(refinement?" with refinement `"+refinement+"`":'')+", but received: `"+print(value)+"`"}=result;return {value,type,refinement,key:path[path.length-1],path,branch,...result,message};}/**
 * Convert a validation result to an iterable of failures.
 */function*toFailures(result,context,struct,value){if(!isIterable(result)){result=[result];}for(const r of result){const failure=toFailure(r,context,struct,value);if(failure){yield failure;}}}/**
 * Check a value against a struct, traversing deeply into nested values, and
 * returning an iterator of failures or success.
 */function*run(value,struct,options){if(options===void 0){options={};}const{path=[],branch=[value],coerce=false,mask=false}=options;const ctx={path,branch};if(coerce){value=struct.coercer(value,ctx);if(mask&&struct.type!=='type'&&isObject(struct.schema)&&isObject(value)&&!Array.isArray(value)){for(const key in value){if(struct.schema[key]===undefined){delete value[key];}}}}let valid=true;for(const failure of struct.validator(value,ctx)){valid=false;yield [failure,undefined];}for(let[k,v,s]of struct.entries(value,ctx)){const ts=run(v,s,{path:k===undefined?path:[...path,k],branch:k===undefined?branch:[...branch,v],coerce,mask});for(const t of ts){if(t[0]){valid=false;yield [t[0],undefined];}else if(coerce){v=t[1];if(k===undefined){value=v;}else if(value instanceof Map){value.set(k,v);}else if(value instanceof Set){value.add(v);}else if(isObject(value)){value[k]=v;}}}}if(valid){for(const failure of struct.refiner(value,ctx)){valid=false;yield [failure,undefined];}}if(valid){yield [undefined,value];}}/**
 * `Struct` objects encapsulate the validation logic for a specific type of
 * values. Once constructed, you use the `assert`, `is` or `validate` helpers to
 * validate unknown input data against the struct.
 */class Struct{constructor(props){this.TYPE=void 0;this.type=void 0;this.schema=void 0;this.coercer=void 0;this.validator=void 0;this.refiner=void 0;this.entries=void 0;const{type,schema,validator,refiner,coercer=value=>value,entries=function*(){}}=props;this.type=type;this.schema=schema;this.entries=entries;this.coercer=coercer;if(validator){this.validator=(value,context)=>{const result=validator(value,context);return toFailures(result,context,this,value);};}else {this.validator=()=>[];}if(refiner){this.refiner=(value,context)=>{const result=refiner(value,context);return toFailures(result,context,this,value);};}else {this.refiner=()=>[];}}/**
   * Assert that a value passes the struct's validation, throwing if it doesn't.
   */assert(value){return assert(value,this);}/**
   * Create a value with the struct's coercion logic, then validate it.
   */create(value){return create(value,this);}/**
   * Check if a value passes the struct's validation.
   */is(value){return is(value,this);}/**
   * Mask a value, coercing and validating it, but returning only the subset of
   * properties defined by the struct's schema.
   */mask(value){return mask(value,this);}/**
   * Validate a value with the struct's validation logic, returning a tuple
   * representing the result.
   *
   * You may optionally pass `true` for the `withCoercion` argument to coerce
   * the value before attempting to validate it. If you do, the result will
   * contain the coerced result when successful.
   */validate(value,options){if(options===void 0){options={};}return validate(value,this,options);}}/**
 * Assert that a value passes a struct, throwing if it doesn't.
 */function assert(value,struct){const result=validate(value,struct);if(result[0]){throw result[0];}}/**
 * Create a value with the coercion logic of struct and validate it.
 */function create(value,struct){const result=validate(value,struct,{coerce:true});if(result[0]){throw result[0];}else {return result[1];}}/**
 * Mask a value, returning only the subset of properties defined by a struct.
 */function mask(value,struct){const result=validate(value,struct,{coerce:true,mask:true});if(result[0]){throw result[0];}else {return result[1];}}/**
 * Check if a value passes a struct.
 */function is(value,struct){const result=validate(value,struct);return !result[0];}/**
 * Validate a value against a struct, returning an error if invalid, or the
 * value (with potential coercion) if valid.
 */function validate(value,struct,options){if(options===void 0){options={};}const tuples=run(value,struct,options);const tuple=shiftIterator(tuples);if(tuple[0]){const error=new StructError(tuple[0],function*(){for(const t of tuples){if(t[0]){yield t[0];}}});return [error,undefined];}else {const v=tuple[1];return [undefined,v];}}function assign(){for(var _len=arguments.length,Structs=new Array(_len),_key=0;_key<_len;_key++){Structs[_key]=arguments[_key];}const isType=Structs[0].type==='type';const schemas=Structs.map(s=>s.schema);const schema=Object.assign({},...schemas);return isType?type(schema):object(schema);}/**
 * Define a new struct type with a custom validation function.
 */function define(name,validator){return new Struct({type:name,schema:null,validator});}/**
 * Create a struct with dynamic validation logic.
 *
 * The callback will receive the value currently being validated, and must
 * return a struct object to validate it with. This can be useful to model
 * validation logic that changes based on its input.
 */function dynamic(fn){return new Struct({type:'dynamic',schema:null,*entries(value,ctx){const struct=fn(value,ctx);yield*struct.entries(value,ctx);},validator(value,ctx){const struct=fn(value,ctx);return struct.validator(value,ctx);},coercer(value,ctx){const struct=fn(value,ctx);return struct.coercer(value,ctx);},refiner(value,ctx){const struct=fn(value,ctx);return struct.refiner(value,ctx);}});}/**
 * Ensure that any value passes validation.
 */function any(){return define('any',()=>true);}function array(Element){return new Struct({type:'array',schema:Element,*entries(value){if(Element&&Array.isArray(value)){for(const[i,v]of value.entries()){yield [i,v,Element];}}},coercer(value){return Array.isArray(value)?value.slice():value;},validator(value){return Array.isArray(value)||"Expected an array value, but received: "+print(value);}});}/**
 * Ensure that a value is a boolean.
 */function boolean(){return define('boolean',value=>{return typeof value==='boolean';});}function enums(values){const schema={};const description=values.map(v=>print(v)).join();for(const key of values){schema[key]=key;}return new Struct({type:'enums',schema,validator(value){return values.includes(value)||"Expected one of `"+description+"`, but received: "+print(value);}});}function literal(constant){const description=print(constant);const t=typeof constant;return new Struct({type:'literal',schema:t==='string'||t==='number'||t==='boolean'?constant:null,validator(value){return value===constant||"Expected the literal `"+description+"`, but received: "+print(value);}});}/**
 * Ensure that no value ever passes validation.
 */function never(){return define('never',()=>false);}/**
 * Ensure that a value is a number.
 */function number(){return define('number',value=>{return typeof value==='number'&&!isNaN(value)||"Expected a number, but received: "+print(value);});}function object(schema){const knowns=schema?Object.keys(schema):[];const Never=never();return new Struct({type:'object',schema:schema?schema:null,*entries(value){if(schema&&isObject(value)){const unknowns=new Set(Object.keys(value));for(const key of knowns){unknowns.delete(key);yield [key,value[key],schema[key]];}for(const key of unknowns){yield [key,value[key],Never];}}},validator(value){return isObject(value)||"Expected an object, but received: "+print(value);},coercer(value){return isObject(value)?{...value}:value;}});}/**
 * Augment a struct to allow `undefined` values.
 */function optional(struct){return new Struct({...struct,validator:(value,ctx)=>value===undefined||struct.validator(value,ctx),refiner:(value,ctx)=>value===undefined||struct.refiner(value,ctx)});}/**
 * Ensure that a value is a string.
 */function string(){return define('string',value=>{return typeof value==='string'||"Expected a string, but received: "+print(value);});}/**
 * Ensure that a value has a set of known properties of specific types.
 *
 * Note: Unrecognized properties are allowed and untouched. This is similar to
 * how TypeScript's structural typing works.
 */function type(schema){const keys=Object.keys(schema);return new Struct({type:'type',schema,*entries(value){if(isObject(value)){for(const k of keys){yield [k,value[k],schema[k]];}}},validator(value){return isObject(value)||"Expected an object, but received: "+print(value);}});}/**
 * Ensure that a value matches one of a set of types.
 */function union(Structs){const description=Structs.map(s=>s.type).join(' | ');return new Struct({type:'union',schema:null,coercer(value,ctx){const firstMatch=Structs.find(s=>{const[e]=s.validate(value,{coerce:true});return !e;})||unknown();return firstMatch.coercer(value,ctx);},validator(value,ctx){const failures=[];for(const S of Structs){const[...tuples]=run(value,S,ctx);const[first]=tuples;if(!first[0]){return [];}else {for(const[failure]of tuples){if(failure){failures.push(failure);}}}}return ["Expected the value to satisfy a union of `"+description+"`, but received: "+print(value),...failures];}});}/**
 * Ensure that any value passes validation, without widening its type to `any`.
 */function unknown(){return define('unknown',()=>true);}/**
 * Augment a `Struct` to add an additional refinement to the validation.
 *
 * The refiner function is guaranteed to receive a value of the struct's type,
 * because the struct's existing validation will already have passed. This
 * allows you to layer additional validation on top of existing structs.
 */function refine(struct,name,refiner){return new Struct({...struct,*refiner(value,ctx){yield*struct.refiner(value,ctx);const result=refiner(value,ctx);const failures=toFailures(result,ctx,struct,value);for(const failure of failures){yield {...failure,refinement:name};}}});}

const MODES_MAX=["queued","parallel"];const baseActionStruct=object({alias:optional(string())});const targetStruct=object({entity_id:optional(union([string(),array(string())])),device_id:optional(union([string(),array(string())])),area_id:optional(union([string(),array(string())]))});assign(baseActionStruct,object({service:optional(string()),service_template:optional(string()),entity_id:optional(string()),target:optional(targetStruct),data:optional(object())}));const playMediaActionStruct=assign(baseActionStruct,object({service:literal("media_player.play_media"),target:optional(object({entity_id:optional(string())})),entity_id:optional(string()),data:object({media_content_id:string(),media_content_type:string()}),metadata:object()}));const activateSceneActionStruct=assign(baseActionStruct,object({service:literal("scene.turn_on"),target:optional(object({entity_id:optional(string())})),entity_id:optional(string()),metadata:object()}));const canRun=state=>{if(state.state==="off"){return true;}if(state.state==="on"&&MODES_MAX.includes(state.attributes.mode)&&state.attributes.current<state.attributes.max){return true;}return false;};const getActionType=action=>{// Check based on config_validation.py#determine_script_action
if("delay"in action){return "delay";}if("wait_template"in action){return "wait_template";}if("condition"in action){return "check_condition";}if("event"in action){return "fire_event";}if("device_id"in action){return "device_action";}if("scene"in action){return "activate_scene";}if("repeat"in action){return "repeat";}if("choose"in action){return "choose";}if("wait_for_trigger"in action){return "wait_for_trigger";}if("variables"in action){return "variables";}if("service"in action){if("metadata"in action){if(is(action,activateSceneActionStruct)){return "activate_scene";}if(is(action,playMediaActionStruct)){return "play_media";}}return "service";}return "unknown";};

const loadGenericDialog=()=>import('./dialog-box-dev.js');const showDialogHelper=(element,dialogParams,extra)=>new Promise(resolve=>{const origCancel=dialogParams.cancel;const origConfirm=dialogParams.confirm;fireEvent(element,"show-dialog",{dialogTag:"dialog-box",dialogImport:loadGenericDialog,dialogParams:{...dialogParams,...extra,cancel:()=>{resolve(extra!==null&&extra!==void 0&&extra.prompt?null:false);if(origCancel){origCancel();}},confirm:out=>{resolve(extra!==null&&extra!==void 0&&extra.prompt?out:true);if(origConfirm){origConfirm(out);}}}});});const showAlertDialog=(element,dialogParams)=>showDialogHelper(element,dialogParams);const showConfirmationDialog=(element,dialogParams)=>showDialogHelper(element,dialogParams,{confirmation:true});const showPromptDialog=(element,dialogParams)=>showDialogHelper(element,dialogParams,{prompt:true});

/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const e=(i,t)=>{var s,o;const n=i._$AN;if(void 0===n)return !1;for(const i of n)null===(o=(s=i)._$AO)||void 0===o||o.call(s,t,!1),e(i,t);return !0;},o=i=>{let t,s;do{if(void 0===(t=i._$AM))break;s=t._$AN,s.delete(i),i=t;}while(0===(null==s?void 0:s.size));},n$1=i=>{for(let t;t=i._$AM;i=t){let s=t._$AN;if(void 0===s)t._$AN=s=new Set();else if(s.has(i))break;s.add(i),l(t);}};function r(i){void 0!==this._$AN?(o(this),this._$AM=i,n$1(this)):this._$AM=i;}function h$1(i,t=!1,s=0){const n=this._$AH,r=this._$AN;if(void 0!==r&&0!==r.size)if(t){if(Array.isArray(n))for(let i=s;i<n.length;i++)e(n[i],!1),o(n[i]);else null!=n&&(e(n,!1),o(n));}else e(this,i);}const l=i=>{var t,e,o,n;i.type==t$1.CHILD&&(null!==(t=(o=i)._$AP)&&void 0!==t||(o._$AP=h$1),null!==(e=(n=i)._$AQ)&&void 0!==e||(n._$AQ=r));};class d extends i$3{constructor(){super(...arguments),this._$AN=void 0;}_$AT(i,t,s){super._$AT(i,t,s),n$1(this),this.isConnected=i._$AU;}_$AO(i,t=!0){var s,n;i!==this.isConnected&&(this.isConnected=i,i?null===(s=this.reconnected)||void 0===s||s.call(this):null===(n=this.disconnected)||void 0===n||n.call(this)),t&&(e(this,i),o(this));}setValue(t){if(r$2(this._$Ct))this._$Ct._$AI(t,this);else {const i=[...this._$Ct._$AH];i[this._$Ci]=t,this._$Ct._$AI(i,this,0);}}disconnected(){}reconnected(){}}

class s{constructor(t){this.U=t;}disconnect(){this.U=void 0;}reconnect(t){this.U=t;}deref(){return this.U;}}class i{constructor(){this.Y=void 0,this.q=void 0;}get(){return this.Y;}pause(){var t;null!==(t=this.Y)&&void 0!==t||(this.Y=new Promise(t=>this.q=t));}resume(){var t;null===(t=this.q)||void 0===t||t.call(this),this.Y=this.q=void 0;}}

/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const n=t=>!t$2(t)&&"function"==typeof t.then;class h extends d{constructor(){super(...arguments),this._$Cft=1073741823,this._$Cwt=[],this._$CG=new s(this),this._$CK=new i();}render(...s){var i;return null!==(i=s.find(t=>!n(t)))&&void 0!==i?i:b;}update(s,i){const r=this._$Cwt;let e=r.length;this._$Cwt=i;const o=this._$CG,h=this._$CK;this.isConnected||this.disconnected();for(let t=0;t<i.length&&!(t>this._$Cft);t++){const s=i[t];if(!n(s))return this._$Cft=t,s;t<e&&s===r[t]||(this._$Cft=1073741823,e=0,Promise.resolve(s).then(async t=>{for(;h.get();)await h.get();const i=o.deref();if(void 0!==i){const r=i._$Cwt.indexOf(s);r>-1&&r<i._$Cft&&(i._$Cft=r,i.setValue(t));}}));}return b;}disconnected(){this._$CG.disconnect(),this._$CK.pause();}reconnected(){this._$CG.reconnect(this),this._$CK.resume();}}const c=e$4(h);

function checkValidDate(date){if(!date){return false;}return date instanceof Date&&!isNaN(date.valueOf());}

// https://regex101.com/r/kc5C14/2
const regExpString="^\\d{4}-(0[1-9]|1[0-2])-([12]\\d|0[1-9]|3[01])";const regExp=new RegExp(regExpString+"$");// 2nd expression without the "end of string" enforced, so it can be used
// to just verify the start of a string and then based on that result e.g.
// check for a full timestamp string efficiently.
const regExpNoStringEnd=new RegExp(regExpString);const isDate=(input,allowCharsAfterDate=false)=>allowCharsAfterDate?regExpNoStringEnd.test(input):regExp.test(input);

// https://stackoverflow.com/a/14322189/1947205
// Changes:
// 1. Do not allow a plus or minus at the start.
// 2. Enforce that we have a "T" or a blank after the date portion
//    to ensure we have a timestamp and not only a date.
// 3. Disallow dates based on week number.
// 4. Disallow dates only consisting of a year.
// https://regex101.com/r/kc5C14/3
const regexp=/^\d{4}-(0[1-9]|1[0-2])-([12]\d|0[1-9]|3[01])[T| ](((([01]\d|2[0-3])((:?)[0-5]\d)?|24:?00)([.,]\d+(?!:))?)(\8[0-5]\d([.,]\d+)?)?([zZ]|([+-])([01]\d|2[0-3]):?([0-5]\d)?)?)$/;const isTimestamp=input=>regexp.test(input);

let jsYamlPromise;const STATE_ATTRIBUTES=["assumed_state","attribution","custom_ui_more_info","custom_ui_state_card","device_class","editable","emulated_hue_name","emulated_hue","entity_picture","friendly_name","haaska_hidden","haaska_name","icon","initial_state","last_reset","restored","state_class","supported_features","unit_of_measurement"];// Convert from internal snake_case format to user-friendly format
function formatAttributeName(value){value=value.replace(/_/g," ").replace(/\bid\b/g,"ID").replace(/\bip\b/g,"IP").replace(/\bmac\b/g,"MAC").replace(/\bgps\b/g,"GPS");return capitalizeFirstLetter(value);}function formatAttributeValue(hass,value){if(value===null){return "—";}// YAML handling
if(Array.isArray(value)&&value.some(val=>val instanceof Object)||!Array.isArray(value)&&value instanceof Object){if(!jsYamlPromise){jsYamlPromise=import('./js-yaml-dump-dev.js');}const yaml=jsYamlPromise.then(jsYaml=>jsYaml.dump(value));return $`<pre>${c(yaml,"")}</pre>`;}if(typeof value==="number"){return formatNumber(value,hass.locale);}if(typeof value==="string"){// URL handling
if(value.startsWith("http")){try{// If invalid URL, exception will be raised
const url=new URL(value);if(url.protocol==="http:"||url.protocol==="https:")return $`<a target="_blank" rel="noreferrer" href=${value}
            >${value}</a
          >`;}catch(_){// Nothing to do here
}}// Date handling
if(isDate(value,true)){// Timestamp handling
if(isTimestamp(value)){const date=new Date(value);if(checkValidDate(date)){return formatDateTimeWithSeconds(date,hass.locale);}}// Value was not a timestamp, so only do date formatting
const date=new Date(value);if(checkValidDate(date)){return formatDate(date,hass.locale);}}}return Array.isArray(value)?value.join(", "):value;}

const fetchUsers=async hass=>hass.callWS({type:"config/auth/list"});const computeUserInitials=name=>{if(!name){return "?";}return name.trim()// Split by space and take first 3 words
.split(" ").slice(0,3)// Of each word, take first letter
.map(s=>s.substring(0,1)).join("");};

const domainToName=(localize,domain,manifest)=>localize(`component.${domain}.title`)||(manifest===null||manifest===void 0?void 0:manifest.name)||domain;const fetchIntegrationManifest=(hass,integration)=>hass.callWS({type:"manifest/get",integration});

const showToast=(el,params)=>fireEvent(el,"hass-notification",params);

const installResizeObserver=async()=>{if(typeof ResizeObserver!=="function"){window.ResizeObserver=(await import('./ResizeObserver.es-dev.js')).default;}};

const getSignedPath=(hass,path)=>hass.callWS({type:"auth/sign_path",path});

export { SUPPORT_VOLUME_SET as $, d as A, BINARY_STATE_ON as B, domainIcon as C, DOMAINS_WITH_CARD as D, DOMAINS_WITH_DYNAMIC_PICTURE as E, fetchUsers as F, DOMAINS_WITH_MORE_INFO as G, DOMAINS_HIDE_DEFAULT_MORE_INFO as H, domainToName as I, showConfirmationDialog as J, showToast as K, DOMAINS_TOGGLE as L, computeActiveState as M, iconColorCSS as N, createCommonjsModule as O, unwrapExports as P, installResizeObserver as Q, DOMAINS_INPUT_ROW as R, STATES_OFF as S, computeMediaDescription as T, UNKNOWN as U, SUPPORT_PREVIOUS_TRACK as V, SUPPORT_PAUSE as W, SUPPORT_STOP as X, SUPPORT_PLAY as Y, SUPPORT_NEXT_TRACK as Z, SUPPORT_TURN_ON as _, UNAVAILABLE as a, SUPPORT_VOLUME_BUTTONS as a0, SUPPORT_TURN_OFF as a1, SUPPORT_VOLUME_MUTE as a2, checkValidDate as a3, UNIT_F as a4, getSignedPath as a5, DOMAINS_MORE_INFO_NO_HISTORY as a6, removeEntityRegistryEntry as a7, updateEntityRegistryEntry as a8, showAlertDialog as a9, computeObjectId as aA, computeUserInitials as aB, getActionType as aC, StructError as aD, refine as aE, dynamic as aF, c as aG, lib as aH, intlLocalematcher_1 as aI, intlLocalematcher_2 as aJ, intlLocalematcher as aK, formatDateYear as aL, formatDateMonthYear as aM, formatDateMonth as aN, formatDateShort as aO, alarmPanelIcon as aP, round as aQ, getCollection as aR, SUPPORT_SEEK as aS, getCurrentProgress as aT, batteryIcon as aU, commonjsGlobal as aV, translationMetadata as aW, BROWSER_PLAYER as aX, browseMediaPlayer as aY, getExtendedEntityRegistryEntry as aa, createCollection as ab, subscribeEntityRegistry as ac, showPromptDialog as ad, formatDateNumeric as ae, computeMediaControls as af, SUPPORT_BROWSE_MEDIA as ag, SUPPORT_SELECT_SOURCE as ah, SUPPORT_SELECT_SOUND_MODE as ai, SUPPORT_PLAY_MEDIA as aj, formatDateWeekday as ak, assign as al, object as am, optional as an, string as ao, boolean as ap, assert as aq, union as ar, array as as, literal as at, type as au, enums as av, any as aw, number as ax, MediaClassBrowserSettings as ay, fetchIntegrationManifest as az, formatDateTime as b, computeStateDomain as c, formatDate as d, computeDomain as e, formatNumber as f, BINARY_STATE_OFF as g, UNAVAILABLE_STATES as h, isNumericState as i, computeStateName as j, forwardHaptic as k, capitalizeFirstLetter as l, computeOpenIcon as m, computeCloseIcon as n, SENSOR_DEVICE_CLASS_TIMESTAMP as o, polyfillsLoaded as p, cleanupMediaTitle as q, canRun as r, supportsFeature as s, STATE_ATTRIBUTES as t, useAmPm as u, formatAttributeName as v, formatAttributeValue as w, numberFormatToLocale as x, formatDateTimeWithSeconds as y, isComponentLoaded as z };
