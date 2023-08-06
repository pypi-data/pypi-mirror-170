const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, f as fireEvent, r, n } from './main-dev.js';
import { s as stopPropagation } from './stop_propagation-dev.js';

_decorate([n("ha-base-time-input")],function(_initialize,_LitElement){class HaBaseTimeInput extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaBaseTimeInput,d:[{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"autoValidate",value(){return false;}},{kind:"field",decorators:[e({type:Boolean})],key:"required",value:void 0},{kind:"field",decorators:[e({type:Number})],key:"format",value(){return 12;}},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[e({type:Number})],key:"hours",value(){return 0;}},{kind:"field",decorators:[e({type:Number})],key:"minutes",value(){return 0;}},{kind:"field",decorators:[e({type:Number})],key:"seconds",value(){return 0;}},{kind:"field",decorators:[e({type:Number})],key:"milliseconds",value(){return 0;}},{kind:"field",decorators:[e()],key:"hourLabel",value(){return "";}},{kind:"field",decorators:[e()],key:"minLabel",value(){return "";}},{kind:"field",decorators:[e()],key:"secLabel",value(){return "";}},{kind:"field",decorators:[e()],key:"millisecLabel",value(){return "";}},{kind:"field",decorators:[e({type:Boolean})],key:"enableSecond",value(){return false;}},{kind:"field",decorators:[e({type:Boolean})],key:"enableMillisecond",value(){return false;}},{kind:"field",decorators:[e({type:Boolean})],key:"noHoursLimit",value(){return false;}},{kind:"field",decorators:[e()],key:"amPm",value(){return "AM";}},{kind:"field",decorators:[e()],key:"value",value:void 0},{kind:"method",key:"render",value:/**
   * Label for the input
   */ /**
   * auto validate time inputs
   */ /**
   * determines if inputs are required
   */ /**
   * 12 or 24 hr format
   */ /**
   * disables the inputs
   */ /**
   * hour
   */ /**
   * minute
   */ /**
   * second
   */ /**
   * milli second
   */ /**
   * Label for the hour input
   */ /**
   * Label for the min input
   */ /**
   * Label for the sec input
   */ /**
   * Label for the milli sec input
   */ /**
   * show the sec field
   */ /**
   * show the milli sec field
   */ /**
   * limit hours input
   */ /**
   * AM or PM
   */ /**
   * Formatted time string
   */function render(){return $`
      ${this.label?$`<label>${this.label}</label>`:""}
      <div class="time-input-wrap">
        <ha-textfield
          id="hour"
          type="number"
          inputmode="numeric"
          .value=${this.hours}
          .label=${this.hourLabel}
          name="hours"
          @input=${this._valueChanged}
          @focus=${this._onFocus}
          no-spinner
          .required=${this.required}
          .autoValidate=${this.autoValidate}
          maxlength="2"
          .max=${this._hourMax}
          min="0"
          .disabled=${this.disabled}
          suffix=":"
          class="hasSuffix"
        >
        </ha-textfield>
        <ha-textfield
          id="min"
          type="number"
          inputmode="numeric"
          .value=${this._formatValue(this.minutes)}
          .label=${this.minLabel}
          @input=${this._valueChanged}
          @focus=${this._onFocus}
          name="minutes"
          no-spinner
          .required=${this.required}
          .autoValidate=${this.autoValidate}
          maxlength="2"
          max="59"
          min="0"
          .disabled=${this.disabled}
          .suffix=${this.enableSecond?":":""}
          class=${this.enableSecond?"has-suffix":""}
        >
        </ha-textfield>
        ${this.enableSecond?$`<ha-textfield
              id="sec"
              type="number"
              inputmode="numeric"
              .value=${this._formatValue(this.seconds)}
              .label=${this.secLabel}
              @input=${this._valueChanged}
              @focus=${this._onFocus}
              name="seconds"
              no-spinner
              .required=${this.required}
              .autoValidate=${this.autoValidate}
              maxlength="2"
              max="59"
              min="0"
              .disabled=${this.disabled}
              .suffix=${this.enableMillisecond?":":""}
              class=${this.enableMillisecond?"has-suffix":""}
            >
            </ha-textfield>`:""}
        ${this.enableMillisecond?$`<ha-textfield
              id="millisec"
              type="number"
              .value=${this._formatValue(this.milliseconds,3)}
              .label=${this.millisecLabel}
              @input=${this._valueChanged}
              @focus=${this._onFocus}
              name="milliseconds"
              no-spinner
              .required=${this.required}
              .autoValidate=${this.autoValidate}
              maxlength="3"
              max="999"
              min="0"
              .disabled=${this.disabled}
            >
            </ha-textfield>`:""}
        ${this.format===24?"":$`<ha-select
              .required=${this.required}
              .value=${this.amPm}
              .disabled=${this.disabled}
              name="amPm"
              naturalMenuWidth
              fixedMenuPosition
              @selected=${this._valueChanged}
              @closed=${stopPropagation}
            >
              <mwc-list-item value="AM">AM</mwc-list-item>
              <mwc-list-item value="PM">PM</mwc-list-item>
            </ha-select>`}
      </div>
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){this[ev.target.name]=ev.target.name==="amPm"?ev.target.value:Number(ev.target.value);const value={hours:this.hours,minutes:this.minutes,seconds:this.seconds,milliseconds:this.milliseconds};if(this.format===12){value.amPm=this.amPm;}fireEvent(this,"value-changed",{value});}},{kind:"method",key:"_onFocus",value:function _onFocus(ev){ev.target.select();}/**
   * Format time fragments
   */},{kind:"method",key:"_formatValue",value:function _formatValue(value,padding=2){return value.toString().padStart(padding,"0");}/**
   * 24 hour format has a max hr of 23
   */},{kind:"get",key:"_hourMax",value:function _hourMax(){if(this.noHoursLimit){return null;}if(this.format===12){return 12;}return 23;}},{kind:"field",static:true,key:"styles",value(){return r`
    :host {
      display: block;
    }
    .time-input-wrap {
      display: flex;
      justify-content: flex-end;
      border-radius: var(--mdc-shape-small, 4px) var(--mdc-shape-small, 4px) 0 0;
      overflow: hidden;
      position: relative;
    }
    ha-textfield {
      width: 40px;
      text-align: center;
      --mdc-shape-small: 0;
      --text-field-appearance: none;
      --text-field-padding: 0 4px;
      --text-field-suffix-padding-left: 2px;
      --text-field-suffix-padding-right: 0;
      --text-field-text-align: center;
    }
    ha-textfield.hasSuffix {
      --text-field-padding: 0 0 0 4px;
    }
    ha-textfield:first-child {
      --text-field-border-top-left-radius: var(--mdc-shape-medium);
    }
    ha-textfield:last-child {
      --text-field-border-top-right-radius: var(--mdc-shape-medium);
    }
    ha-select {
      --mdc-shape-small: 0;
      width: 85px;
    }
    label {
      -moz-osx-font-smoothing: grayscale;
      -webkit-font-smoothing: antialiased;
      font-family: var(
        --mdc-typography-body2-font-family,
        var(--mdc-typography-font-family, Roboto, sans-serif)
      );
      font-size: var(--mdc-typography-body2-font-size, 0.875rem);
      line-height: var(--mdc-typography-body2-line-height, 1.25rem);
      font-weight: var(--mdc-typography-body2-font-weight, 400);
      letter-spacing: var(
        --mdc-typography-body2-letter-spacing,
        0.0178571429em
      );
      text-decoration: var(--mdc-typography-body2-text-decoration, inherit);
      text-transform: var(--mdc-typography-body2-text-transform, inherit);
      color: var(--mdc-theme-text-primary-on-background, rgba(0, 0, 0, 0.87));
      padding-left: 4px;
    }
  `;}}]};},s);
