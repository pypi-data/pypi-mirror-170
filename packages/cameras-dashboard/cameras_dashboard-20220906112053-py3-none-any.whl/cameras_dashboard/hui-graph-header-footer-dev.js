const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, af as y, r, n } from './main-dev.js';
import './ha-circular-progress-dev.js';
import { W as findEntities, X as hasConfigOrEntityChanged, Y as fetchRecent } from './ha-more-info-dialog-dev.js';
import { e as computeDomain } from './auth-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './stop_propagation-dev.js';
import './repeat-dev.js';

const strokeWidth=5;

const average=items=>items.reduce((sum,entry)=>sum+parseFloat(entry.state),0)/items.length;const lastValue=items=>parseFloat(items[items.length-1].state)||0;const calcPoints=(history,hours,width,detail,min,max)=>{const coords=[];const height=80;let yRatio=(max-min)/height;yRatio=yRatio!==0?yRatio:height;let xRatio=width/(hours-(detail===1?1:0));xRatio=isFinite(xRatio)?xRatio:width;const first=history.filter(Boolean)[0];let last=[average(first),lastValue(first)];const getCoords=(item,i,offset=0,depth=1)=>{if(depth>1&&item){return item.forEach((subItem,index)=>getCoords(subItem,i,index,depth-1));}const x=xRatio*(i+offset/6);if(item){last=[average(item),lastValue(item)];}const y=height+strokeWidth/2-((item?last[0]:last[1])-min)/yRatio;return coords.push([x,y]);};for(let i=0;i<history.length;i+=1){getCoords(history[i],i,0,detail);}if(coords.length===1){coords[1]=[width,coords[0][1]];}coords.push([width,coords[coords.length-1][1]]);return coords;};const coordinates=(history,hours,width,detail,limits)=>{history.forEach(item=>{item.state=Number(item.state);});history=history.filter(item=>!Number.isNaN(item.state));const min=(limits===null||limits===void 0?void 0:limits.min)!==undefined?limits.min:Math.min(...history.map(item=>item.state));const max=(limits===null||limits===void 0?void 0:limits.max)!==undefined?limits.max:Math.max(...history.map(item=>item.state));const now=new Date().getTime();const reduce=(res,item,point)=>{const age=now-new Date(item.last_changed).getTime();let key=Math.abs(age/(1000*3600)-hours);if(point){key=(key-Math.floor(key))*60;key=Number((Math.round(key/10)*10).toString()[0]);}else {key=Math.floor(key);}if(!res[key]){res[key]=[];}res[key].push(item);return res;};history=history.reduce((res,item)=>reduce(res,item,false),[]);if(detail>1){history=history.map(entry=>entry.reduce((res,item)=>reduce(res,item,true),[]));}if(!history.length){return undefined;}return calcPoints(history,hours,width,detail,min,max);};

const midPoint=(_Ax,_Ay,_Bx,_By)=>{const _Zx=(_Ax-_Bx)/2+_Bx;const _Zy=(_Ay-_By)/2+_By;return [_Zx,_Zy];};const getPath=coords=>{if(!coords.length){return "";}let next;let Z;const X=0;const Y=1;let path="";let last=coords.filter(Boolean)[0];path+=`M ${last[X]},${last[Y]}`;for(const coord of coords){next=coord;Z=midPoint(last[X],last[Y],next[X],next[Y]);path+=` ${Z[X]},${Z[Y]}`;path+=` Q${next[X]},${next[Y]}`;last=next;}path+=` ${next[X]},${next[Y]}`;return path;};

_decorate([n("hui-graph-base")],function(_initialize,_LitElement){class HuiGraphBase extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiGraphBase,d:[{kind:"field",decorators:[e()],key:"coordinates",value:void 0},{kind:"field",decorators:[t()],key:"_path",value:void 0},{kind:"method",key:"render",value:function render(){return $`
      ${this._path?y`<svg width="100%" height="100%" viewBox="0 0 500 100">
          <g>
            <mask id="fill">
              <path
                class='fill'
                fill='white'
                d="${this._path} L 500, 100 L 0, 100 z"
              />
            </mask>
            <rect height="100%" width="100%" id="fill-rect" fill="var(--accent-color)" mask="url(#fill)"></rect>
            <mask id="line">
              <path
                fill="none"
                stroke="var(--accent-color)"
                stroke-width="${strokeWidth}"
                stroke-linecap="round"
                stroke-linejoin="round"
                d=${this._path}
              ></path>
            </mask>
            <rect height="100%" width="100%" id="rect" fill="var(--accent-color)" mask="url(#line)"></rect>
          </g>
        </svg>`:y`<svg width="100%" height="100%" viewBox="0 0 500 100"></svg>`}
    `;}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){if(!this.coordinates){return;}if(changedProps.has("coordinates")){this._path=getPath(this.coordinates);}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: flex;
        width: 100%;
        border-radius: 1.5rem;
      }
      .fill {
        opacity: 0.1;
      }
    `;}}]};},s);

const MINUTE=60000;const HOUR=MINUTE*60;const includeDomains=["counter","input_number","number","sensor"];let HuiGraphHeaderFooter=_decorate([n("hui-graph-header-footer")],function(_initialize,_LitElement){class HuiGraphHeaderFooter extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiGraphHeaderFooter,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-graph-footer-editor-dev.js');return document.createElement("hui-graph-footer-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFallback){const maxEntities=1;const entityFilter=stateObj=>!isNaN(Number(stateObj.state))&&!!stateObj.attributes.unit_of_measurement;const foundEntities=findEntities(hass,maxEntities,entities,entitiesFallback,includeDomains,entityFilter);return {type:"graph",entity:foundEntities[0]||""};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"type",value:void 0},{kind:"field",decorators:[e()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_coordinates",value:void 0},{kind:"field",key:"_date",value:void 0},{kind:"field",key:"_stateHistory",value:void 0},{kind:"field",key:"_fetching",value(){return false;}},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!(config!==null&&config!==void 0&&config.entity)||!includeDomains.includes(computeDomain(config.entity))){throw new Error("Missing sensor entity");}const cardConfig={detail:1,hours_to_show:24,...config};cardConfig.hours_to_show=Number(cardConfig.hours_to_show);cardConfig.detail=cardConfig.detail===1||cardConfig.detail===2?cardConfig.detail:1;this._config=cardConfig;}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}if(!this._coordinates){return $`
        <div class="container">
          <ha-circular-progress active size="small"></ha-circular-progress>
        </div>
      `;}if(!this._coordinates.length){return $`
        <div class="container">
          <div class="info">No state history.</div>
        </div>
      `;}return $`
      <hui-graph-base .coordinates=${this._coordinates}></hui-graph-base>
    `;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"updated",value:function updated(changedProps){if(!this._config||!this.hass||this._fetching&&!changedProps.has("_config")){return;}if(changedProps.has("_config")){const oldConfig=changedProps.get("_config");if(!oldConfig||oldConfig.entity!==this._config.entity){this._stateHistory=[];}this._getCoordinates();}else if(Date.now()-this._date.getTime()>=MINUTE){this._getCoordinates();}}},{kind:"method",key:"_getCoordinates",value:async function _getCoordinates(){var _this$_stateHistory;this._fetching=true;const endTime=new Date();const startTime=!this._date||!((_this$_stateHistory=this._stateHistory)!==null&&_this$_stateHistory!==void 0&&_this$_stateHistory.length)?new Date(new Date().setHours(endTime.getHours()-this._config.hours_to_show)):this._date;if(this._stateHistory.length){const inHoursToShow=[];const outHoursToShow=[];// Split into inside and outside of "hours to show".
this._stateHistory.forEach(entity=>(endTime.getTime()-new Date(entity.last_changed).getTime()<=this._config.hours_to_show*HOUR?inHoursToShow:outHoursToShow).push(entity));if(outHoursToShow.length){// If we have values that are now outside of "hours to show", re-add the last entry. This could e.g. be
// the "initial state" from the history backend. Without it, it would look like there is no history data
// at the start at all in the database = graph would start suddenly instead of on the left side of the card.
inHoursToShow.push(outHoursToShow[outHoursToShow.length-1]);}this._stateHistory=inHoursToShow;}const stateHistory=await fetchRecent(this.hass,this._config.entity,startTime,endTime,Boolean(this._stateHistory.length));if(stateHistory.length&&stateHistory[0].length){this._stateHistory.push(...stateHistory[0]);}this._coordinates=coordinates(this._stateHistory,this._config.hours_to_show,500,this._config.detail,this._config.limits)||[];this._date=endTime;this._fetching=false;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-circular-progress {
        position: absolute;
        top: calc(50% - 14px);
      }
      .container {
        display: flex;
        justify-content: center;
        position: relative;
        padding-bottom: 20%;
      }
      .info {
        position: absolute;
        top: calc(50% - 16px);
        color: var(--secondary-text-color);
      }
    `;}}]};},s);

export { HuiGraphHeaderFooter };
