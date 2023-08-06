const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, G as i, $, dH as mdiMagnify, at as mdiClose, f as fireEvent, r, n } from './main-dev.js';

_decorate([n("search-input-round")],function(_initialize,_LitElement){class SearchInputRound extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:SearchInputRound,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"filter",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"suffix",value(){return false;}},{kind:"field",decorators:[e({type:Boolean})],key:"autofocus",value(){return false;}},{kind:"field",decorators:[e({type:String})],key:"label",value:void 0},{kind:"method",key:"focus",value:function focus(){var _this$_input;(_this$_input=this._input)===null||_this$_input===void 0?void 0:_this$_input.focus();}},{kind:"field",decorators:[i("ha-textfield",true)],key:"_input",value:void 0},{kind:"method",key:"render",value:function render(){return $`
      <ha-textfield
        class="rounded"
        outlined
        .autofocus=${this.autofocus}
        .label=${this.label||"Search"}
        .value=${this.filter||""}
        icon
        .iconTrailing=${this.filter||this.suffix}
        @input=${this._filterInputChanged}
      >
        <slot name="prefix" slot="leadingIcon">
          <ha-svg-icon tabindex="-1" class="prefix" .path=${mdiMagnify}></ha-svg-icon>
        </slot>
        <div class="trailing" slot="trailingIcon">
          ${this.filter&&$`
            <ha-icon-button
              @click=${this._clearSearch}
              .label=${this.hass.localize("ui.common.clear")}
              .path=${mdiClose}
              class="clear-button"
            ></ha-icon-button>
          `}
          <slot name="suffix"></slot>
        </div>
      </ha-textfield>
    `;}},{kind:"method",key:"_filterChanged",value:async function _filterChanged(value){fireEvent(this,"value-changed",{value:String(value)});}},{kind:"method",key:"_filterInputChanged",value:async function _filterInputChanged(e){this._filterChanged(e.target.value);}},{kind:"method",key:"_clearSearch",value:async function _clearSearch(){this._filterChanged("");}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        display: inline-flex;
      }
      ha-svg-icon,
      ha-icon-button {
        color: var(--primary-text-color);
      }
      ha-svg-icon {
        outline: none;
      }
      .clear-button {
        --mdc-icon-size: 20px;
      }
      ha-textfield.rounded {
        --mdc-shape-small: 28px;
        width: 100%;
      }
      .trailing {
        display: flex;
        align-items: center;
      }
    `;}}]};},s);
