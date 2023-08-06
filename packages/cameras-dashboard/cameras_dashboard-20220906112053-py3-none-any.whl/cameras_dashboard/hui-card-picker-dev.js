const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, n, c as s, d as e, t, b as memoizeOne, $, I as i, f as fireEvent, z as o, r, dD as Fuse } from './main-dev.js';
import { J as getCardElementClass, K as customCards, M as tryCreateCardElement, N as getCustomCardEntry, O as CUSTOM_TYPE_PREFIX } from './ha-more-info-dialog-dev.js';
import { H as HuiElementEditor } from './hui-element-editor-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-header-bar-dev.js';
import { h as UNAVAILABLE_STATES, aG as c } from './auth-dev.js';
import './ha-circular-progress-dev.js';

_decorate([n("hui-card-element-editor")],function(_initialize,_HuiElementEditor){class HuiCardElementEditor extends _HuiElementEditor{constructor(...args){super(...args);_initialize(this);}}return {F:HuiCardElementEditor,d:[{kind:"method",key:"getConfigElement",value:async function getConfigElement(){const elClass=await getCardElementClass(this.configElementType);// Check if a GUI editor exists
if(elClass&&elClass.getConfigElement){return elClass.getConfigElement();}return undefined;}}]};},HuiElementEditor);

const EXCLUDED_DOMAINS=["zone","persistent_notification"];const addFromAction=(entities,actionConfig)=>{if(actionConfig.action!=="call-service"||!actionConfig.service_data||!actionConfig.service_data.entity_id){return;}let entityIds=actionConfig.service_data.entity_id;if(!Array.isArray(entityIds)){entityIds=[entityIds];}for(const entityId of entityIds){entities.add(entityId);}};const addEntityId=(entities,entity)=>{if(typeof entity==="string"){entities.add(entity);return;}if(entity.entity){entities.add(entity.entity);}if(entity.camera_image){entities.add(entity.camera_image);}if(entity.tap_action){addFromAction(entities,entity.tap_action);}if(entity.hold_action){addFromAction(entities,entity.hold_action);}};const addEntities=(entities,obj)=>{if(obj.entity){addEntityId(entities,obj.entity);}if(obj.entities&&Array.isArray(obj.entities)){obj.entities.forEach(entity=>addEntityId(entities,entity));}if(obj.card){addEntities(entities,obj.card);}if(obj.cards&&Array.isArray(obj.cards)){obj.cards.forEach(card=>addEntities(entities,card));}if(obj.elements&&Array.isArray(obj.elements)){obj.elements.forEach(card=>addEntities(entities,card));}if(obj.badges&&Array.isArray(obj.badges)){obj.badges.forEach(badge=>addEntityId(entities,badge));}};const computeUsedEntities=config=>{const entities=new Set();config.views.forEach(view=>addEntities(entities,view));return entities;};const calcUnusedEntities=(hass,usedEntities)=>{const unusedEntities=new Set();for(const entity of Object.keys(hass.states)){if(!usedEntities.has(entity)&&!EXCLUDED_DOMAINS.includes(entity.split(".",1)[0])){unusedEntities.add(entity);}}return unusedEntities;};

const getCardStubConfig=async(hass,type,entities,entitiesFallback)=>{let cardConfig={type};const elClass=await getCardElementClass(type);if(elClass&&elClass.getStubConfig){const classStubConfig=await elClass.getStubConfig(hass,entities,entitiesFallback);cardConfig={...cardConfig,...classStubConfig};}return cardConfig;};

const coreCards=[{type:"alarm-panel",showElement:true},{type:"button",showElement:true},// {
//   type: "calendar",
//   showElement: true,
// },
{type:"entities",showElement:true},// {
//   type: "entity",
//   showElement: true,
// },
{type:"gauge",showElement:true},// {
//   type: "glance",
//   showElement: true,
// },
// {
//   type: "history-graph",
//   showElement: true,
// },
// {
//   type: "statistics-graph",
//   showElement: false,
// },
// {
//   type: "humidifier",
//   showElement: true,
// },
{type:"light",showElement:true},// {
//   type: "map",
//   showElement: true,
// },
// {
//   type: "markdown",
//   showElement: true,
// },
// {
//   type: "media-control",
//   showElement: true,
// },
// {
//   type: "picture",
//   showElement: true,
// },
// {
//   type: "picture-elements",
//   showElement: true,
// },
{type:"picture-entity",showElement:true},{type:"picture-camera",showElement:true},// {
//   type: "picture-glance",
//   showElement: true,
// },
// {
//   type: "plant-status",
//   showElement: true,
// },
{type:"sensor",showElement:true},{type:"thermostat",showElement:true},{type:"weather-forecast",showElement:true}// {
//   type: "area",
//   showElement: true,
// },
// {
//   type: "conditional",
// },
// {
//   type: "entity-filter",
// },
// {
//   type: "grid",
// },
// {
//   type: "horizontal-stack",
// },
// {
//   type: "iframe",
// },
// {
//   type: "logbook",
// },
// {
//   type: "vertical-stack",
// },
// {
//   type: "shopping-list",
// },
];

_decorate([n("hui-card-picker")],function(_initialize,_LitElement){class HuiCardPicker extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiCardPicker,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_cards",value(){return [];}},{kind:"field",key:"lovelace",value:void 0},{kind:"field",key:"cardPicked",value:void 0},{kind:"field",decorators:[t()],key:"_filter",value(){return "";}},{kind:"field",decorators:[t()],key:"_width",value:void 0},{kind:"field",decorators:[t()],key:"_height",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"virginity",value(){return true;}},{kind:"field",key:"_unusedEntities",value:void 0},{kind:"field",key:"_usedEntities",value:void 0},{kind:"field",key:"_filterCards",value(){return memoizeOne((cardElements,filter)=>{if(!filter){return cardElements;}let cards=cardElements.map(cardElement=>cardElement.card);const options={keys:["type","name","description"],isCaseSensitive:false,minMatchCharLength:2,threshold:0.2};const fuse=new Fuse(cards,options);cards=fuse.search(filter).map(result=>result.item);return cardElements.filter(cardElement=>cards.includes(cardElement.card));});}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.lovelace||!this._unusedEntities||!this._usedEntities){return $``;}return $`
      <search-input
        .hass=${this.hass}
        .filter=${this._filter}
        @value-changed=${this._handleSearchChange}
        .label=${this.hass.localize("ui.panel.lovelace.editor.edit_card.search_cards")}
      ></search-input>
      <div
        id="content"
        style=${i({width:this._width?`${this._width}px`:"auto",height:this._height?`${this._height}px`:"auto"})}
      >
        <div class="cards-container">
          ${this._filterCards(this._cards,this._filter).map(cardElement=>cardElement.element)}
        </div>
      </div>
    `;}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){const oldHass=changedProps.get("hass");if(!oldHass){return true;}if(oldHass.locale!==this.hass.locale){return true;}return false;}},{kind:"method",key:"firstUpdated",value:function firstUpdated(){if(!this.hass||!this.lovelace){return;}const usedEntities=computeUsedEntities(this.lovelace);const unusedEntities=calcUnusedEntities(this.hass,usedEntities);this._usedEntities=[...usedEntities].filter(eid=>this.hass.states[eid]&&!UNAVAILABLE_STATES.includes(this.hass.states[eid].state));this._unusedEntities=[...unusedEntities].filter(eid=>this.hass.states[eid]&&!UNAVAILABLE_STATES.includes(this.hass.states[eid].state));this._loadCards();}},{kind:"method",key:"_loadCards",value:function _loadCards(){let cards=coreCards.map(card=>({name:this.hass.localize(`ui.panel.lovelace.editor.card.${card.type}.name`),description:this.hass.localize(`ui.panel.lovelace.editor.card.${card.type}.description`),...card}));if(customCards.length>0){const customCardToRemove=["Browser Player"];// add the rest
// TODO: discover type
cards=customCards.filter(ccard=>!customCardToRemove.includes(ccard.name?ccard.name:"")).map(ccard=>({type:ccard.type,name:ccard.name,description:ccard.description,showElement:ccard.preview,isCustom:true})).concat(cards);}this._cards=cards.map(card=>({card:card,element:$`${c(this._renderCardElement(card),$`
          <div class="card spinner">
            <ha-circular-progress active alt="Loading"></ha-circular-progress>
          </div>
        `)}`}));}},{kind:"method",key:"_handleSearchChange",value:function _handleSearchChange(ev){const value=ev.detail.value;if(!value){// Reset when we no longer filter
this._width=undefined;this._height=undefined;}else if(!this._width||!this._height){// Save height and width so the dialog doesn't jump while searching
const div=this.shadowRoot.getElementById("content");if(div&&!this._width){const width=div.clientWidth;if(width){this._width=width;}}if(div&&!this._height){const height=div.clientHeight;if(height){this._height=height;}}}this._filter=value;}},{kind:"method",key:"_cardPicked",value:function _cardPicked(ev){let config=ev.currentTarget.config;if(config.type!=="grid"&&this.virginity){config={type:"grid",cards:[config]};}fireEvent(this,"config-changed",{config});}},{kind:"method",key:"_tryCreateCardElement",value:function _tryCreateCardElement(cardConfig){const element=tryCreateCardElement(cardConfig);element.hass=this.hass;element.addEventListener("ll-rebuild",ev=>{ev.stopPropagation();this._rebuildCard(element,cardConfig);},{once:true});return element;}},{kind:"method",key:"_rebuildCard",value:function _rebuildCard(cardElToReplace,config){let newCardEl;try{newCardEl=this._tryCreateCardElement(config);}catch(err){return;}if(cardElToReplace.parentElement){cardElToReplace.parentElement.replaceChild(newCardEl,cardElToReplace);}}},{kind:"method",key:"_renderCardElement",value:async function _renderCardElement(card){let{type}=card;const{showElement,isCustom,name,description}=card;const customCard=isCustom?getCustomCardEntry(type):undefined;if(isCustom){type=`${CUSTOM_TYPE_PREFIX}${type}`;}let element;let cardConfig={type};if(this.hass&&this.lovelace){cardConfig=await getCardStubConfig(this.hass,type,this._unusedEntities,this._usedEntities);if(showElement){try{element=this._tryCreateCardElement(cardConfig);}catch(err){element=undefined;}}}return $`
      <div class="card">
        <div
          class="overlay"
          @click=${this._cardPicked}
          .config=${cardConfig}
        ></div>
        <div
          class="preview ${o({description:!element||element.tagName==="HUI-ERROR-CARD"})}"
        >
          ${element&&element.tagName!=="HUI-ERROR-CARD"?element:customCard?this.hass.localize(`ui.panel.lovelace.editor.card.${customCard.description}`)||customCard.description:description}
        </div>
        <div class="card-header">
          ${customCard?`${this.hass.localize(`ui.panel.lovelace.editor.card.${customCard.type}`)||customCard.name||customCard.type}`:name}
        </div>
      </div>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return [r`
        search-input {
          display: block;
          --mdc-shape-small: var(--card-picker-search-shape);
          /* margin: var(--card-picker-search-margin); */
          margin: 0%;
        }

        .cards-container {
          display: grid;
          grid-gap: 8px 8px;
          grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
          margin-top: 20px;
          justify-items: center;
          justify-content: center;
        }

        .card {
          height: 100%;
          width: 100%;
          max-width: 400px;
          display: flex;
          flex-direction: column;
          border-radius: var(--ha-card-border-radius, 4px);
          background: var(--primary-background-color, #fafafa);
          cursor: pointer;
          position: relative;
          overflow: hidden;
          border-radius: 1.5rem;
        }
        @media only screen and (max-width: 390px) {
          .card {
            height: 100%;
            max-width: 67vw;
            display: flex;
            flex-direction: column;
            border-radius: var(--ha-card-border-radius, 4px);
            background: var(--primary-background-color, #fafafa);
            cursor: pointer;
            position: relative;
            overflow: hidden;
            border-radius: 1.5rem;
          }
        }

        .card-header {
          color: var(--app-header-text-color);
          font-family: var(--ha-card-header-font-family, inherit);
          font-size: 16px;
          font-weight: bold;
          letter-spacing: -0.012em;
          line-height: 20px;
          padding: 12px 16px;
          display: block;
          text-align: center;
          background: var(--header-card-picker-background);
          border-top: 1px solid var(--divider-color);
        }

        .preview {
          pointer-events: none;
          margin: 20px;
          flex-grow: 1;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .preview > :first-child {
          zoom: 0.9;
          display: block;
          width: 100%;
        }

        .description {
          text-align: center;
        }

        .spinner {
          align-items: center;
          justify-content: center;
        }

        .overlay {
          position: absolute;
          width: 100%;
          height: 100%;
          z-index: 1;
          box-sizing: border-box;
          border: var(--ha-card-border-width, 1px) solid
            var(--ha-card-border-color, var(--divider-color));
          border-radius: 1.5rem;
        }

        .manual {
          max-width: none;
        }
      `];}}]};},s);
