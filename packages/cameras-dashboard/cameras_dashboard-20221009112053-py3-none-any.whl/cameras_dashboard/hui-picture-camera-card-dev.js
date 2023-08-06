const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, R as e$1, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, $, z as o, Q as l, r, T as RippleHandlers, K as e$2, n } from './main-dev.js';
import { e as computeDomain, j as computeStateName, a as UNAVAILABLE } from './auth-dev.js';
import { W as findEntities, X as hasConfigOrEntityChanged, Z as createEntityNotFoundWarning, o as computeStateDisplay, Q as actionHandler, R as hasAction, T as handleAction } from './ha-more-info-dialog-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-picture-camera-card")],function(_initialize,_LitElement){class HuiPictureEntityCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiPictureEntityCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-picture-camera-card-editor-dev.js');return document.createElement("hui-picture-camera-card-editor");}},{kind:"field",decorators:[e({type:String})],key:"layout",value(){return "big";}},{kind:"field",decorators:[e({type:Boolean})],key:"toggleCam",value(){return false;}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(hass,entities,entitiesFallback){const maxEntities=1;const foundEntities=findEntities(hass,maxEntities,entities,entitiesFallback,["camera"]);return {type:"picture-camera",entity:foundEntities[0]||"",camera_image:""};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[e$1("mwc-ripple")],key:"_ripple",value:void 0},{kind:"field",decorators:[t()],key:"_shouldRenderRipple",value(){return false;}},{kind:"method",key:"getCardSize",value:function getCardSize(){return 3;}},{kind:"method",key:"setConfig",value:function setConfig(config){if(!config||!config.entity){throw new Error("Entity must be specified");}if(computeDomain(config.entity)!=="camera"&&!config.image&&!config.state_image&&!config.camera_image){throw new Error("No image source configured");}this._config={show_name:true,show_state:true,...config};}},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){return hasConfigOrEntityChanged(this,changedProps);}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiPictureEntityCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass){return;}const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(!oldHass||!oldConfig||oldHass.themes!==this.hass.themes||oldConfig.theme!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}}},{kind:"method",key:"render",value:function render(){var _this$_config,_this$_config2,_this$_config3,_this$_config4,_this$_config5,_this$_config6,_this$_config7,_this$_config8,_this$_config9,_this$_config10;if(!this._config||!this.hass){return $``;}const stateObj=this.hass.states[this._config.entity];if(!stateObj){return $`
        <hui-warning>
          ${createEntityNotFoundWarning(this.hass,this._config.entity)}
        </hui-warning>
      `;}const name=this._config.name||computeStateName(stateObj);computeStateDisplay(this.hass.localize,stateObj,this.hass.locale);let footer="";if(this._config.show_name&&this._config.show_state){footer=$`
        <div class="footer both">
          <div>${name}</div>
          <svg
            class="togcam"
            width="50"
            height="50"
            viewBox="0 0 50 50"
            fill="#FFFFFF"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M31.21 38.19H7.46997C5.80997 38.19 4.46997 36.85 4.46997 35.19V13.46C4.46997 11.8 5.80997 10.46 7.46997 10.46H31.21C32.87 10.46 34.21 11.8 34.21 13.46V35.19C34.21 36.85 32.87 38.19 31.21 38.19Z M28.0699 23.4799L41.6499 13.1899C42.3499 12.6599 43.3499 13.1599 43.3499 14.0399V34.6299C43.3499 35.5099 42.3499 35.9999 41.6499 35.4799L28.0699 25.1699C27.5099 24.7499 27.5099 23.8999 28.0699 23.4799Z"
            />
          </svg>
        </div>
      `;}else if(this._config.show_name){footer=$`<div class="footer single">${name}</div>`;}return $`
      ${this.layout!=="small"?$` <ha-card class="ha-card-og">
            <!-- <button-recorder></button-recorder> -->
            ${stateObj.state===UNAVAILABLE?$`<unavailable-icon></unavailable-icon>`:$``}
            <hui-image
              class=${o({"hui-image-medium":this.layout==="medium","hui-image-big":this.layout==="big"})}
              .hass=${this.hass}
              .image=${(_this$_config=this._config)===null||_this$_config===void 0?void 0:_this$_config.image}
              .stateImage=${(_this$_config2=this._config)===null||_this$_config2===void 0?void 0:_this$_config2.state_image}
              .stateFilter=${(_this$_config3=this._config)===null||_this$_config3===void 0?void 0:_this$_config3.state_filter}
              .cameraImage=${computeDomain(this._config.entity)==="camera"?(_this$_config4=this._config)===null||_this$_config4===void 0?void 0:_this$_config4.entity:(_this$_config5=this._config)===null||_this$_config5===void 0?void 0:_this$_config5.camera_image}
              .cameraView=${(_this$_config6=this._config)===null||_this$_config6===void 0?void 0:_this$_config6.camera_view}
              .entity=${(_this$_config7=this._config)===null||_this$_config7===void 0?void 0:_this$_config7.entity}
              .aspectRatio=${(_this$_config8=this._config)===null||_this$_config8===void 0?void 0:_this$_config8.aspect_ratio}
              @action=${this._handleAction}
              .actionHandler=${actionHandler({hasHold:hasAction(this._config.hold_action),hasDoubleClick:hasAction(this._config.double_tap_action)})}
              tabindex=${l(hasAction((_this$_config9=this._config)===null||_this$_config9===void 0?void 0:_this$_config9.tap_action)||(_this$_config10=this._config)!==null&&_this$_config10!==void 0&&_this$_config10.entity?"0":undefined)}
            >
            </hui-image>
            ${footer}
          </ha-card>`:$`
            ${/* @click=${ this._handleAction }
                @focus=${ this.handleRippleFocus }
                @blur=${ this.handleRippleBlur }
                @mousedown=${ this.handleRippleActivate }
                @mouseup=${ this.handleRippleDeactivate }
                @touchstart=${ this.handleRippleActivate }
                @touchend=${ this.handleRippleDeactivate }
                @touchcancel=${ this.handleRippleDeactivate }
                @keydown=${ this._handleKeyDown }
              */$``}
            <ha-card
              @click=${this._handleAction}
              @focus=${this.handleRippleFocus}
              @blur=${this.handleRippleBlur}
              @mousedown=${this.handleRippleActivate}
              @mouseup=${this.handleRippleDeactivate}
              @touchstart=${this.handleRippleActivate}
              @touchend=${this.handleRippleDeactivate}
              @touchcancel=${this.handleRippleDeactivate}
              @keydown=${this._handleKeyDown}
              class=${o({"ha-card-small":this.layout==="small"})}
            >
              <!-- <button-recorder></button-recorder> -->
              ${stateObj.state===UNAVAILABLE?$` <svg
                      class="ha-status-icon-small"
                      width="50"
                      height="50"
                      viewBox="0 0 50 50"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        d="M31.21 38.19H7.46997C5.80997 38.19 4.46997 36.85 4.46997 35.19V13.46C4.46997 11.8 5.80997 10.46 7.46997 10.46H31.21C32.87 10.46 34.21 11.8 34.21 13.46V35.19C34.21 36.85 32.87 38.19 31.21 38.19Z M28.0699 23.4799L41.6499 13.1899C42.3499 12.6599 43.3499 13.1599 43.3499 14.0399V34.6299C43.3499 35.5099 42.3499 35.9999 41.6499 35.4799L28.0699 25.1699C27.5099 24.7499 27.5099 23.8999 28.0699 23.4799Z"
                      />
                      <path
                        d="M32.45 42.9499L33.73 41.9799C34.15 41.6599 34.23 41.0699 33.91 40.6599L7.55 5.87988C7.23 5.46988 6.64 5.37988 6.23 5.69988L4.95 6.66988C4.53 6.98988 4.45 7.57988 4.77 7.98988L31.14 42.7699C31.44 43.1799 32.04 43.2699 32.45 42.9499Z"
                        fill="#999999"
                      />
                    </svg>
                    <unavailable-icon></unavailable-icon>`:$`<svg
                    class="ha-status-icon-small"
                    width="50"
                    height="50"
                    viewBox="0 0 50 50"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M31.21 38.19H7.46997C5.80997 38.19 4.46997 36.85 4.46997 35.19V13.46C4.46997 11.8 5.80997 10.46 7.46997 10.46H31.21C32.87 10.46 34.21 11.8 34.21 13.46V35.19C34.21 36.85 32.87 38.19 31.21 38.19Z M28.0699 23.4799L41.6499 13.1899C42.3499 12.6599 43.3499 13.1599 43.3499 14.0399V34.6299C43.3499 35.5099 42.3499 35.9999 41.6499 35.4799L28.0699 25.1699C27.5099 24.7499 27.5099 23.8999 28.0699 23.4799Z"
                    />
                  </svg> `}
              <span class="rect-card-small" tabindex="-1" .title=${name}
                >${name}</span
              >
              ${this._shouldRenderRipple?$`<mwc-ripple></mwc-ripple>`:""}
            </ha-card>
          `}
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      .ha-card-og {
        min-height: 75px;
        overflow: hidden;
        position: relative;
        height: 100%;
        box-sizing: border-box;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 1.5rem;
      }

      .ha-card-medium {
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: left;
        text-align: left;
        padding: 4% 0;
        font-size: 1.5rem;
        height: 100%;
        box-sizing: border-box;
        justify-content: center;
        position: relative;
        overflow: hidden;
        border-radius: 1.5rem;
        font-weight: 450;
      }
      .ha-card-small {
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: left;
        text-align: left;
        padding: 4% 0;
        font-size: 1.2rem;
        height: 100%;
        box-sizing: border-box;
        justify-content: center;
        position: relative;
        overflow: hidden;
        border-radius: 1.5rem;
        font-weight: 450;
      }
      .rect-card-small {
        padding: 5%;
        padding-bottom: 4%;
        margin-bottom: 4%;
        margin-left: 7%;
        white-space: nowrap;
        display: inline-block;
        overflow: hidden;
        max-width: 110px;
        /* float: left; */
        text-overflow: ellipsis;
      }
      .ha-status-icon-small {
        width: 63%;
        height: auto;
        fill: var(--paper-item-icon-color, #44739e);
        --mdc-icon-size: 100%;
        margin-left: 5%;
      }

      hui-image {
        width: 100%;
        cursor: pointer;
      }

      .footer {
        /* start paper-font-common-nowrap style */
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        /* end paper-font-common-nowrap style */

        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: var(
          --ha-picture-card-background-color,
          rgba(0, 0, 0, 0.3)
        );
        padding: 16px;
        font-size: 16px;
        line-height: 16px;
        color: var(--ha-picture-card-text-color, white);
      }

      .both {
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      .togcam {
        width: 24px;
        height: 24px;
      }

      .single {
        text-align: center;
      }
    `;}},{kind:"method",key:"_handleAction",value:function _handleAction(ev){handleAction(this,this.hass,this._config,ev.detail.action);}},{kind:"field",key:"_rippleHandlers",value(){return new RippleHandlers(()=>{this._shouldRenderRipple=true;return this._ripple;});}},{kind:"method",key:"_handleKeyDown",value:function _handleKeyDown(ev){if(ev.key==="Enter"||ev.key===" "){handleAction(this,this.hass,this._config,"tap");}}},{kind:"method",decorators:[e$2({passive:true})],key:"handleRippleActivate",value:function handleRippleActivate(evt){this._rippleHandlers.startPress(evt);}},{kind:"method",key:"handleRippleDeactivate",value:function handleRippleDeactivate(){this._rippleHandlers.endPress();}},{kind:"method",key:"handleRippleFocus",value:function handleRippleFocus(){this._rippleHandlers.startFocus();}},{kind:"method",key:"handleRippleBlur",value:function handleRippleBlur(){this._rippleHandlers.endFocus();}}]};},s);
