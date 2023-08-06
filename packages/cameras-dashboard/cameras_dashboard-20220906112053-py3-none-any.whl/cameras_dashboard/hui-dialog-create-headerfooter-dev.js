const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { eT as mdiChartBellCurveCumulative, aS as mdiGestureTapButton, eU as mdiImageArea, _ as _decorate, c as s, d as e, t, f as fireEvent, $, ax as haStyleDialog, r, n } from './main-dev.js';
import { b as createCloseHeading } from './ha-header-bar-dev.js';
import { G as getHeaderFooterElementClass } from './ha-more-info-dialog-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const headerFooterElements=[{type:"graph",icon:mdiChartBellCurveCumulative},{type:"buttons",icon:mdiGestureTapButton},{type:"picture",icon:mdiImageArea}];

const getHeaderFooterStubConfig=async(hass,type,entities,entitiesFallback)=>{let config={type};const elClass=await getHeaderFooterElementClass(type);if(elClass&&elClass.getStubConfig){const classStubConfig=await elClass.getStubConfig(hass,entities,entitiesFallback);config={...config,...classStubConfig};}return config;};

let HuiCreateDialogHeaderFooter=_decorate([n("hui-dialog-create-headerfooter")],function(_initialize,_LitElement){class HuiCreateDialogHeaderFooter extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiCreateDialogHeaderFooter,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_params",value:void 0},{kind:"method",key:"showDialog",value:async function showDialog(params){this._params=params;}},{kind:"method",key:"closeDialog",value:function closeDialog(){this._params=undefined;fireEvent(this,"dialog-closed",{dialog:this.localName});return true;}},{kind:"method",key:"render",value:function render(){if(!this._params){return $``;}return $`
      <ha-dialog
        open
        scrimClickAction
        .heading=${createCloseHeading(this.hass,this.hass.localize(`ui.panel.lovelace.editor.header-footer.choose_header_footer`,"type",this.hass.localize(`ui.panel.lovelace.editor.header-footer.${this._params.type}`)))}
        @keydown=${this._ignoreKeydown}
        @closed=${this._cancel}
      >
        <div class="elements">
          ${headerFooterElements.map((headerFooter,index)=>$`
                <ha-card
                  role="button"
                  tabindex="0"
                  aria-labeledby=${"card-name-"+index}
                  outlined
                  .type=${headerFooter.type}
                  @click=${this._handleHeaderFooterPicked}
                  @keyDown=${this._handleHeaderFooterPicked}
                  dialogInitialFocus
                >
                  <ha-svg-icon .path=${headerFooter.icon}></ha-svg-icon>
                  <div .id=${"card-name-"+index} role="none presentation">
                    ${this.hass.localize(`ui.panel.lovelace.editor.header-footer.types.${headerFooter.type}.name`)}
                  </div>
                </ha-card>
              `)}
        </div>
        <div slot="primaryAction">
          <mwc-button @click=${this._cancel}>
            ${this.hass.localize("ui.common.cancel")}
          </mwc-button>
        </div>
      </ha-dialog>
    `;}},{kind:"method",key:"_handleHeaderFooterPicked",value:async function _handleHeaderFooterPicked(ev){if(ev instanceof KeyboardEvent&&ev.key!=="Enter"&&ev.key!==" "&&ev.key!=="Spacebar"){return;}const type=ev.currentTarget.type;let config={type};if(this.hass){var _this$_params;config=await getHeaderFooterStubConfig(this.hass,type,((_this$_params=this._params)===null||_this$_params===void 0?void 0:_this$_params.entities)||[],[]);}this._params.pickHeaderFooter(config);this.closeDialog();}},{kind:"method",key:"_ignoreKeydown",value:function _ignoreKeydown(ev){ev.stopPropagation();}},{kind:"method",key:"_cancel",value:function _cancel(ev){if(ev){ev.stopPropagation();}this.closeDialog();}},{kind:"get",static:true,key:"styles",value:function styles(){return [haStyleDialog,r`
        @media all and (max-width: 450px), all and (max-height: 500px) {
          /* overrule the ha-style-dialog max-height on small screens */
          ha-dialog {
            --mdc-dialog-max-height: 100%;
            height: 100%;
          }
        }

        @media all and (min-width: 850px) {
          ha-dialog {
            --mdc-dialog-min-width: 550px;
          }
        }

        ha-dialog {
          --mdc-dialog-max-width: 550px;
          --dialog-content-padding: 2px 24px 20px 24px;
          --dialog-z-index: 5;
        }

        .elements {
          display: flex;
          flex-wrap: wrap;
        }

        .spinner,
        ha-card {
          width: calc(50% - 8px);
          text-align: center;
          margin: 4px;
        }

        ha-card {
          box-sizing: border-box;
          padding: 8px;
          color: var(--secondary-text-color);
          font-size: 16px;
          cursor: pointer;
        }

        ha-svg-icon {
          padding-bottom: 4px;
          --mdc-icon-size: 38px;
        }
      `];}}]};},s);

export { HuiCreateDialogHeaderFooter };
