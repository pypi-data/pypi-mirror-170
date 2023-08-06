const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { ah as __decorate, G as i, d as e, em as TextFieldBase, $, z as o, Q as l, en as l$1, r, _ as _decorate, j as _get, k as _getPrototypeOf, eo as styles$1, n } from './main-dev.js';

const booleanOrStringConverter={fromAttribute(value){if(value===null){return false;}else if(value===''){return true;}return value;},toAttribute(value){if(typeof value==='boolean'){return value?'':null;}return value;}};/** @soyCompatible */class TextAreaBase extends TextFieldBase{constructor(){super(...arguments);this.rows=2;this.cols=20;this.charCounter=false;}/** @soyTemplate */render(){const shouldRenderCharCounter=this.charCounter&&this.maxLength!==-1;const shouldRenderInternalCharCounter=shouldRenderCharCounter&&this.charCounter==='internal';const shouldRenderExternalCharCounter=shouldRenderCharCounter&&!shouldRenderInternalCharCounter;const shouldRenderHelperText=!!this.helper||!!this.validationMessage||shouldRenderExternalCharCounter;/** @classMap */const classes={'mdc-text-field--disabled':this.disabled,'mdc-text-field--no-label':!this.label,'mdc-text-field--filled':!this.outlined,'mdc-text-field--outlined':this.outlined,'mdc-text-field--end-aligned':this.endAligned,'mdc-text-field--with-internal-counter':shouldRenderInternalCharCounter};return $`
      <label class="mdc-text-field mdc-text-field--textarea ${o(classes)}">
        ${this.renderRipple()}
        ${this.outlined?this.renderOutline():this.renderLabel()}
        ${this.renderInput()}
        ${this.renderCharCounter(shouldRenderInternalCharCounter)}
        ${this.renderLineRipple()}
      </label>
      ${this.renderHelperText(shouldRenderHelperText,shouldRenderExternalCharCounter)}
    `;}/** @soyTemplate */renderInput(){const ariaLabelledbyOrUndef=!!this.label?'label':undefined;const minOrUndef=this.minLength===-1?undefined:this.minLength;const maxOrUndef=this.maxLength===-1?undefined:this.maxLength;const autocapitalizeOrUndef=this.autocapitalize?this.autocapitalize:undefined;return $`
      <textarea
          aria-labelledby=${l(ariaLabelledbyOrUndef)}
          class="mdc-text-field__input"
          .value="${l$1(this.value)}"
          rows="${this.rows}"
          cols="${this.cols}"
          ?disabled="${this.disabled}"
          placeholder="${this.placeholder}"
          ?required="${this.required}"
          ?readonly="${this.readOnly}"
          minlength="${l(minOrUndef)}"
          maxlength="${l(maxOrUndef)}"
          name="${l(this.name===''?undefined:this.name)}"
          inputmode="${l(this.inputMode)}"
          autocapitalize="${l(autocapitalizeOrUndef)}"
          @input="${this.handleInputChange}"
          @blur="${this.onInputBlur}">
      </textarea>`;}}__decorate([i('textarea')],TextAreaBase.prototype,"formElement",void 0);__decorate([e({type:Number})],TextAreaBase.prototype,"rows",void 0);__decorate([e({type:Number})],TextAreaBase.prototype,"cols",void 0);__decorate([e({converter:booleanOrStringConverter})],TextAreaBase.prototype,"charCounter",void 0);

const styles=r`.mdc-text-field{height:100%}.mdc-text-field__input{resize:none}`;

_decorate([n("ha-textarea")],function(_initialize,_TextAreaBase){class HaTextArea extends _TextAreaBase{constructor(...args){super(...args);_initialize(this);}}return {F:HaTextArea,d:[{kind:"field",decorators:[e({type:Boolean,reflect:true})],key:"autogrow",value(){return false;}},{kind:"method",key:"updated",value:function updated(changedProperties){_get(_getPrototypeOf(HaTextArea.prototype),"updated",this).call(this,changedProperties);if(this.autogrow&&changedProperties.has("value")){this.mdcRoot.dataset.value=this.value+'=\u200B"';// add a zero-width space to correctly wrap
}}},{kind:"field",static:true,key:"styles",value(){return [styles$1,styles,r`
      :host([autogrow]) {
        max-height: 200px;
      }
      :host([autogrow]) .mdc-text-field {
        position: relative;
        min-height: 74px;
        min-width: 178px;
      }
      :host([autogrow]) .mdc-text-field:after {
        content: attr(data-value);
        margin-top: 23px;
        margin-bottom: 9px;
        line-height: 1.5rem;
        min-height: 42px;
        padding: 0px 32px 0 16px;
        letter-spacing: var(
          --mdc-typography-subtitle1-letter-spacing,
          0.009375em
        );
        visibility: hidden;
        white-space: pre-wrap;
      }
      :host([autogrow]) .mdc-text-field__input {
        position: absolute;
        height: calc(100% - 32px);
      }
      :host([autogrow]) .mdc-text-field.mdc-text-field--no-label:after {
        margin-top: 16px;
        margin-bottom: 16px;
      }
    `];}}]};},TextAreaBase);

const brandsUrl=options=>`/local/brands/${options.domain}/icon.png`;const extractDomainFromBrandUrl=url=>url.split("/")[4];

export { brandsUrl as b, extractDomainFromBrandUrl as e };
