const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, G as i, $, z as o, r, n } from './main-dev.js';
import { F as FORMAT_NUMBER, c as callAlarmAction } from './alarm_control_panel-dev.js';

const BUTTONS=["1","2","3","4","5","6","7","8","9","","0","clear"];const ARM_ACTIONS=["arm_away","arm_home"];const DISARM_ACTIONS=["disarm"];let MoreInfoAlarmControlPanel=_decorate([n("more-info-alarm_control_panel")],function(_initialize,_LitElement){class MoreInfoAlarmControlPanel extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoAlarmControlPanel,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"stateObj",value:void 0},{kind:"field",decorators:[i("#alarmCode")],key:"_input",value:void 0},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.stateObj){return $``;}return $`
      <div class="actions">
        ${(this.stateObj.state==="disarmed"?ARM_ACTIONS:DISARM_ACTIONS).map(stateAction=>$`
            <mwc-button
              .action=${stateAction}
              @click=${this._handleActionClick}
              outlined
            >
              ${this.hass.localize(`ui.card.alarm_control_panel.${stateAction}`)}
            </mwc-button>
          `)}
      </div>
      ${!this.stateObj.attributes.code_format?"":$`
            <div class="center">
              <ha-textfield
                id="alarmCode"
                .label=${this.hass.localize("ui.card.alarm_control_panel.code")}
                type="password"
                .inputmode=${this.stateObj.attributes.code_format===FORMAT_NUMBER?"numeric":"text"}
              ></ha-textfield>
            </div>
          `}
      ${this.stateObj.attributes.code_format!==FORMAT_NUMBER?"":$`
            <div id="keypad">
              ${BUTTONS.map(value=>value===""?$`<mwc-button disabled></mwc-button>`:$`
                      <mwc-button
                        .value=${value}
                        @click=${this._handlePadClick}
                        outlined
                        class=${o({numberkey:value!=="clear"})}
                      >
                        ${value==="clear"?this.hass.localize(`ui.card.alarm_control_panel.clear_code`):value}
                      </mwc-button>
                    `)}
            </div>
          `}
    `;}},{kind:"method",key:"_handlePadClick",value:function _handlePadClick(e){const val=e.currentTarget.value;this._input.value=val==="clear"?"":this._input.value+val;}},{kind:"method",key:"_handleActionClick",value:function _handleActionClick(e){const input=this._input;callAlarmAction(this.hass,this.stateObj.entity_id,e.currentTarget.action,(input===null||input===void 0?void 0:input.value)||undefined);if(input){input.value="";}}},{kind:"field",static:true,key:"styles",value(){return r`
    ha-textfield {
      display: block;
      margin: 8px;
      max-width: 150px;
      text-align: center;
    }

    #keypad {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      margin: auto;
      width: 100%;
      max-width: 300px;
    }

    #keypad mwc-button {
      padding: 8px;
      width: 30%;
      box-sizing: border-box;
    }

    .actions {
      margin: 0;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
    }

    .actions mwc-button {
      margin: 0 4px 4px;
    }

    mwc-button#disarm {
      color: var(--error-color);
    }

    mwc-button.numberkey {
      --mdc-typography-button-font-size: var(--keypad-font-size, 0.875rem);
    }

    .center {
      display: flex;
      justify-content: center;
    }
  `;}}]};},s);

export { MoreInfoAlarmControlPanel };
