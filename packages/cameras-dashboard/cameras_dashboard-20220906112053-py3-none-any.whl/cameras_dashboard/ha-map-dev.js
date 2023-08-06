const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, I as i, f as fireEvent, r, l as a, t, j as _get, k as _getPrototypeOf, n } from './main-dev.js';
import { j as computeStateName, c as computeStateDomain, Q as installResizeObserver } from './auth-dev.js';

// Sets up a Leaflet map on the provided DOM element
const setupLeafletMap=async(mapElement,darkMode)=>{if(!mapElement.parentNode){throw new Error("Cannot setup Leaflet map on disconnected element");}// eslint-disable-next-line
const Leaflet=(await import('./leaflet-src-dev.js')).default;Leaflet.Icon.Default.imagePath="/static/images/leaflet/images/";const map=Leaflet.map(mapElement);const style=document.createElement("link");style.setAttribute("href","/static/images/leaflet/leaflet.css");style.setAttribute("rel","stylesheet");mapElement.parentNode.appendChild(style);map.setView([52.3731339,4.8903147],13);const tileLayer=createTileLayer(Leaflet,Boolean(darkMode)).addTo(map);return [map,Leaflet,tileLayer];};const replaceTileLayer=(leaflet,map,tileLayer,darkMode)=>{map.removeLayer(tileLayer);tileLayer=createTileLayer(leaflet,darkMode);tileLayer.addTo(map);return tileLayer;};const createTileLayer=(leaflet,darkMode)=>leaflet.tileLayer(`https://{s}.basemaps.cartocdn.com/${darkMode?"dark_all":"light_all"}/{z}/{x}/{y}${leaflet.Browser.retina?"@2x.png":".png"}`,{attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>',subdomains:"abcd",minZoom:0,maxZoom:20});

let HaEntityMarker=_decorate(null,function(_initialize,_LitElement){class HaEntityMarker extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaEntityMarker,d:[{kind:"field",decorators:[e({attribute:"entity-id"})],key:"entityId",value:void 0},{kind:"field",decorators:[e({attribute:"entity-name"})],key:"entityName",value:void 0},{kind:"field",decorators:[e({attribute:"entity-picture"})],key:"entityPicture",value:void 0},{kind:"field",decorators:[e({attribute:"entity-color"})],key:"entityColor",value:void 0},{kind:"method",key:"render",value:function render(){return $`
      <div
        class="marker"
        style=${i({"border-color":this.entityColor})}
        @click=${this._badgeTap}
      >
        ${this.entityPicture?$`<div
              class="entity-picture"
              style=${i({"background-image":`url(${this.entityPicture})`})}
            ></div>`:this.entityName}
      </div>
    `;}},{kind:"method",key:"_badgeTap",value:function _badgeTap(ev){ev.stopPropagation();if(this.entityId){fireEvent(this,"hass-more-info",{entityId:this.entityId});}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .marker {
        display: flex;
        justify-content: center;
        align-items: center;
        box-sizing: border-box;
        overflow: hidden;
        width: 48px;
        height: 48px;
        font-size: var(--ha-marker-font-size, 1.5em);
        border-radius: 50%;
        border: 1px solid var(--ha-marker-color, var(--primary-color));
        color: var(--primary-text-color);
        background-color: var(--card-background-color);
      }
      .entity-picture {
        background-size: cover;
        height: 100%;
        width: 100%;
      }
    `;}}]};},s);customElements.define("ha-entity-marker",HaEntityMarker);

const getEntityId=entity=>typeof entity==="string"?entity:entity.entity_id;_decorate([n("ha-map")],function(_initialize,_ReactiveElement){class HaMap extends _ReactiveElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaMap,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"entities",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"paths",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"layers",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"autoFit",value(){return false;}},{kind:"field",decorators:[e({type:Boolean})],key:"fitZones",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"darkMode",value:void 0},{kind:"field",decorators:[e({type:Number})],key:"zoom",value(){return 14;}},{kind:"field",decorators:[t()],key:"_loaded",value(){return false;}},{kind:"field",key:"leafletMap",value:void 0},{kind:"field",key:"Leaflet",value:void 0},{kind:"field",key:"_tileLayer",value:void 0},{kind:"field",key:"_resizeObserver",value:void 0},{kind:"field",key:"_mapItems",value(){return [];}},{kind:"field",key:"_mapZones",value(){return [];}},{kind:"field",key:"_mapPaths",value(){return [];}},{kind:"method",key:"connectedCallback",value:function connectedCallback(){_get(_getPrototypeOf(HaMap.prototype),"connectedCallback",this).call(this);this._loadMap();this._attachObserver();}},{kind:"method",key:"disconnectedCallback",value:function disconnectedCallback(){_get(_getPrototypeOf(HaMap.prototype),"disconnectedCallback",this).call(this);if(this.leafletMap){this.leafletMap.remove();this.leafletMap=undefined;this.Leaflet=undefined;}this._loaded=false;if(this._resizeObserver){this._resizeObserver.unobserve(this);}}},{kind:"method",key:"update",value:function update(changedProps){var _this$darkMode;_get(_getPrototypeOf(HaMap.prototype),"update",this).call(this,changedProps);if(!this._loaded){return;}const oldHass=changedProps.get("hass");if(changedProps.has("_loaded")||changedProps.has("entities")){this._drawEntities();}else if(this._loaded&&oldHass&&this.entities){// Check if any state has changed
for(const entity of this.entities){if(oldHass.states[getEntityId(entity)]!==this.hass.states[getEntityId(entity)]){this._drawEntities();break;}}}if(changedProps.has("_loaded")||changedProps.has("paths")){this._drawPaths();}if(changedProps.has("_loaded")||changedProps.has("layers")){this._drawLayers(changedProps.get("layers"));}if(changedProps.has("_loaded")||(changedProps.has("entities")||changedProps.has("layers"))&&this.autoFit){this.fitMap();}if(changedProps.has("zoom")){this.leafletMap.setZoom(this.zoom);}if(!changedProps.has("darkMode")&&(!changedProps.has("hass")||oldHass&&oldHass.themes.darkMode===this.hass.themes.darkMode)){return;}const darkMode=(_this$darkMode=this.darkMode)!==null&&_this$darkMode!==void 0?_this$darkMode:this.hass.themes.darkMode;this._tileLayer=replaceTileLayer(this.Leaflet,this.leafletMap,this._tileLayer,darkMode);this.shadowRoot.getElementById("map").classList.toggle("dark",darkMode);}},{kind:"method",key:"_loadMap",value:async function _loadMap(){var _this$darkMode2;let map=this.shadowRoot.getElementById("map");if(!map){map=document.createElement("div");map.id="map";this.shadowRoot.append(map);}const darkMode=(_this$darkMode2=this.darkMode)!==null&&_this$darkMode2!==void 0?_this$darkMode2:this.hass.themes.darkMode;[this.leafletMap,this.Leaflet,this._tileLayer]=await setupLeafletMap(map,darkMode);this.shadowRoot.getElementById("map").classList.toggle("dark",darkMode);this._loaded=true;}},{kind:"method",key:"fitMap",value:function fitMap(){var _this$layers,_this$layers2;if(!this.leafletMap||!this.Leaflet||!this.hass){return;}if(!this._mapItems.length&&!((_this$layers=this.layers)!==null&&_this$layers!==void 0&&_this$layers.length)){this.leafletMap.setView(new this.Leaflet.LatLng(this.hass.config.latitude,this.hass.config.longitude),this.zoom);return;}let bounds=this.Leaflet.latLngBounds(this._mapItems?this._mapItems.map(item=>item.getLatLng()):[]);if(this.fitZones){var _this$_mapZones;(_this$_mapZones=this._mapZones)===null||_this$_mapZones===void 0?void 0:_this$_mapZones.forEach(zone=>{bounds.extend("getBounds"in zone?zone.getBounds():zone.getLatLng());});}(_this$layers2=this.layers)===null||_this$layers2===void 0?void 0:_this$layers2.forEach(layer=>{bounds.extend("getBounds"in layer?layer.getBounds():layer.getLatLng());});if(!this.layers){bounds=bounds.pad(0.5);}this.leafletMap.fitBounds(bounds,{maxZoom:this.zoom});}},{kind:"method",key:"_drawLayers",value:function _drawLayers(prevLayers){if(prevLayers){prevLayers.forEach(layer=>layer.remove());}if(!this.layers){return;}const map=this.leafletMap;this.layers.forEach(layer=>{map.addLayer(layer);});}},{kind:"method",key:"_drawPaths",value:function _drawPaths(){const hass=this.hass;const map=this.leafletMap;const Leaflet=this.Leaflet;if(!hass||!map||!Leaflet){return;}if(this._mapPaths.length){this._mapPaths.forEach(marker=>marker.remove());this._mapPaths=[];}if(!this.paths){return;}const darkPrimaryColor=getComputedStyle(this).getPropertyValue("--dark-primary-color");this.paths.forEach(path=>{let opacityStep;let baseOpacity;if(path.gradualOpacity){opacityStep=path.gradualOpacity/(path.points.length-2);baseOpacity=1-path.gradualOpacity;}for(let pointIndex=0;pointIndex<path.points.length-1;pointIndex++){const opacity=path.gradualOpacity?baseOpacity+pointIndex*opacityStep:undefined;// DRAW point
this._mapPaths.push(Leaflet.circleMarker(path.points[pointIndex],{radius:3,color:path.color||darkPrimaryColor,opacity,fillOpacity:opacity,interactive:false}));// DRAW line between this and next point
this._mapPaths.push(Leaflet.polyline([path.points[pointIndex],path.points[pointIndex+1]],{color:path.color||darkPrimaryColor,opacity,interactive:false}));}const pointIndex=path.points.length-1;if(pointIndex>=0){const opacity=path.gradualOpacity?baseOpacity+pointIndex*opacityStep:undefined;// DRAW end path point
this._mapPaths.push(Leaflet.circleMarker(path.points[pointIndex],{radius:3,color:path.color||darkPrimaryColor,opacity,fillOpacity:opacity,interactive:false}));}this._mapPaths.forEach(marker=>map.addLayer(marker));});}},{kind:"method",key:"_drawEntities",value:function _drawEntities(){var _this$darkMode3;const hass=this.hass;const map=this.leafletMap;const Leaflet=this.Leaflet;if(!hass||!map||!Leaflet){return;}if(this._mapItems.length){this._mapItems.forEach(marker=>marker.remove());this._mapItems=[];}if(this._mapZones.length){this._mapZones.forEach(marker=>marker.remove());this._mapZones=[];}if(!this.entities){return;}const computedStyles=getComputedStyle(this);const zoneColor=computedStyles.getPropertyValue("--accent-color");const darkPrimaryColor=computedStyles.getPropertyValue("--dark-primary-color");const className=((_this$darkMode3=this.darkMode)!==null&&_this$darkMode3!==void 0?_this$darkMode3:this.hass.themes.darkMode)?"dark":"light";for(const entity of this.entities){const stateObj=hass.states[getEntityId(entity)];if(!stateObj){continue;}const title=computeStateName(stateObj);const{latitude,longitude,passive,icon,radius,entity_picture:entityPicture,gps_accuracy:gpsAccuracy}=stateObj.attributes;if(!(latitude&&longitude)){continue;}if(computeStateDomain(stateObj)==="zone"){// DRAW ZONE
if(passive){continue;}// create icon
let iconHTML="";if(icon){const el=document.createElement("ha-icon");el.setAttribute("icon",icon);iconHTML=el.outerHTML;}else {const el=document.createElement("span");el.innerHTML=title;iconHTML=el.outerHTML;}// create marker with the icon
this._mapZones.push(Leaflet.marker([latitude,longitude],{icon:Leaflet.divIcon({html:iconHTML,iconSize:[24,24],className}),interactive:false,title}));// create circle around it
this._mapZones.push(Leaflet.circle([latitude,longitude],{interactive:false,color:zoneColor,radius}));continue;}// DRAW ENTITY
// create icon
const entityName=title.split(" ").map(part=>part[0]).join("").substr(0,3);// create marker with the icon
this._mapItems.push(Leaflet.marker([latitude,longitude],{icon:Leaflet.divIcon({html:`
              <ha-entity-marker
                entity-id="${getEntityId(entity)}"
                entity-name="${entityName}"
                entity-picture="${entityPicture?this.hass.hassUrl(entityPicture):""}"
                ${typeof entity!=="string"?`entity-color="${entity.color}"`:""}
              ></ha-entity-marker>
            `,iconSize:[48,48],className:""}),title:computeStateName(stateObj)}));// create circle around if entity has accuracy
if(gpsAccuracy){this._mapItems.push(Leaflet.circle([latitude,longitude],{interactive:false,color:darkPrimaryColor,radius:gpsAccuracy}));}}this._mapItems.forEach(marker=>map.addLayer(marker));this._mapZones.forEach(marker=>map.addLayer(marker));}},{kind:"method",key:"_attachObserver",value:async function _attachObserver(){if(!this._resizeObserver){await installResizeObserver();this._resizeObserver=new ResizeObserver(()=>{var _this$leafletMap;(_this$leafletMap=this.leafletMap)===null||_this$leafletMap===void 0?void 0:_this$leafletMap.invalidateSize({debounceMoveend:true});});}this._resizeObserver.observe(this);}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: block;
        height: 300px;
      }
      #map {
        height: 100%;
      }
      #map.dark {
        background: #090909;
      }
      .light {
        color: #000000;
      }
      .dark {
        color: #ffffff;
      }
      .leaflet-marker-draggable {
        cursor: move !important;
      }
      .leaflet-edit-resize {
        border-radius: 50%;
        cursor: nesw-resize !important;
      }
      .named-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        text-align: center;
        color: var(--primary-text-color);
      }
    `;}}]};},a);
