const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { ah as __decorate, n, G as i, d as e, dQ as ListItemBase, $, z as o, r, _ as _decorate, dR as styles$2 } from './main-dev.js';
import { s as styles$1, C as CheckboxBase } from './mwc-checkbox.css-dev.js';

/** @soyCompatible */let Checkbox=class Checkbox extends CheckboxBase{};Checkbox.styles=[styles$1];Checkbox=__decorate([n('mwc-checkbox')],Checkbox);

class CheckListItemBase extends ListItemBase{constructor(){super(...arguments);this.left=false;this.graphic='control';}render(){const checkboxClasses={'mdc-deprecated-list-item__graphic':this.left,'mdc-deprecated-list-item__meta':!this.left};const text=this.renderText();const graphic=this.graphic&&this.graphic!=='control'&&!this.left?this.renderGraphic():$``;const meta=this.hasMeta&&this.left?this.renderMeta():$``;const ripple=this.renderRipple();return $`
      ${ripple}
      ${graphic}
      ${this.left?'':text}
      <span class=${o(checkboxClasses)}>
        <mwc-checkbox
            reducedTouchTarget
            tabindex=${this.tabindex}
            .checked=${this.selected}
            ?disabled=${this.disabled}
            @change=${this.onChange}>
        </mwc-checkbox>
      </span>
      ${this.left?text:''}
      ${meta}`;}async onChange(evt){const checkbox=evt.target;const changeFromProp=this.selected===checkbox.checked;if(!changeFromProp){this._skipPropRequest=true;this.selected=checkbox.checked;await this.updateComplete;this._skipPropRequest=false;}}}__decorate([i('slot')],CheckListItemBase.prototype,"slotElement",void 0);__decorate([i('mwc-checkbox')],CheckListItemBase.prototype,"checkboxElement",void 0);__decorate([e({type:Boolean})],CheckListItemBase.prototype,"left",void 0);__decorate([e({type:String,reflect:true})],CheckListItemBase.prototype,"graphic",void 0);

const styles=r`:host(:not([twoline])){height:56px}:host(:not([left])) .mdc-deprecated-list-item__meta{height:40px;width:40px}`;

_decorate([n("ha-check-list-item")],function(_initialize,_CheckListItemBase){class HaCheckListItem extends _CheckListItemBase{constructor(...args){super(...args);_initialize(this);}}return {F:HaCheckListItem,d:[{kind:"field",static:true,key:"styles",value(){return [styles$2,styles,r`
      :host {
        --mdc-theme-secondary: var(--primary-color);
      }
      .mdc-deprecated-list-item__graphic {
        pointer-events: none;
      }
    `];}}]};},CheckListItemBase);
