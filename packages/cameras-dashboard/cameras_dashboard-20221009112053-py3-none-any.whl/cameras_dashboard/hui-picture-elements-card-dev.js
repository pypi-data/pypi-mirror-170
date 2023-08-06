const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, $, r, n } from './main-dev.js';
import { W as findEntities, ar as createStyledHuiElement } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-picture-elements-card")],function(_initialize,_LitElement){class HuiPictureElementsCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiPictureElementsCard,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_elements",value:void 0},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFallback){const maxEntities=1;const foundEntities=findEntities(hass,maxEntities,entities,entitiesFallback,["sensor","binary_sensor"]);return {type:"picture-elements",elements:[{type:"state-badge",entity:foundEntities[0]||"",style:{top:"32%",left:"40%"}}],image:"https://demo.home-assistant.io/stub_config/floorplan.png"};}},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return 4;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config){throw new Error("Invalid configuration");}else if(!(config.image||config.camera_image||config.state_image)||config.state_image&&!config.entity){throw new Error("Image required");}else if(!Array.isArray(config.elements)){throw new Error("Elements required");}this._config=config;this._elements=this._config.elements.map(elementConfig=>{const element=createStyledHuiElement(elementConfig);if(this.hass){element.hass=this.hass;}return element;});}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiPictureElementsCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass){return;}if(this._elements&&changedProps.has("hass")){for(const element of this._elements){element.hass=this.hass;}}const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(!oldHass||!oldConfig||oldHass.themes!==this.hass.themes||oldConfig.theme!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}return $`
      <ha-card .header=${this._config.title}>
        <div id="root">
          <hui-image
            .hass=${this.hass}
            .image=${this._config.image}
            .stateImage=${this._config.state_image}
            .stateFilter=${this._config.state_filter}
            .cameraImage=${this._config.camera_image}
            .cameraView=${this._config.camera_view}
            .entity=${this._config.entity}
            .aspectRatio=${this._config.aspect_ratio}
            .darkModeFilter=${this._config.dark_mode_filter}
            .darkModeImage=${this._config.dark_mode_image}
          ></hui-image>
          ${this._elements}
        </div>
      </ha-card>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      #root {
        position: relative;
      }

      .element {
        position: absolute;
        transform: translate(-50%, -50%);
      }

      ha-card {
        overflow: hidden;
        height: 100%;
        box-sizing: border-box;
      }
    `;}}]};},s);
