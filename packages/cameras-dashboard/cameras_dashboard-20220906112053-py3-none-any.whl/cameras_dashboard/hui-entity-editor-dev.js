const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, $, ep as mdiDrag, f as fireEvent, r, n } from './main-dev.js';
import { i } from './guard-dev.js';
import './ha-entity-picker-dev.js';
import { s as sortableStyles } from './process-editor-entities-dev.js';

let Sortable;_decorate([n("hui-entity-editor")],function(_initialize,_LitElement){class HuiEntityEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEntityEditor,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"entities",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[t()],key:"_attached",value(){return false;}},{kind:"field",decorators:[t()],key:"_renderEmptySortable",value(){return false;}},{kind:"field",key:"_sortable",value:void 0},{kind:"method",key:"connectedCallback",value:function connectedCallback(){_get(_getPrototypeOf(HuiEntityEditor.prototype),"connectedCallback",this).call(this);this._attached=true;}},{kind:"method",key:"disconnectedCallback",value:function disconnectedCallback(){_get(_getPrototypeOf(HuiEntityEditor.prototype),"disconnectedCallback",this).call(this);this._attached=false;}},{kind:"method",key:"render",value:function render(){if(!this.entities){return $``;}const includeDomainsEntityPicker=["cover","fan","light","switch","sensor"];return $`
      <h3>
        ${this.label||this.hass.localize("ui.panel.lovelace.editor.card.generic.entities")+" ("+this.hass.localize("ui.panel.lovelace.editor.card.config.required")+")"}
      </h3>
      <div class="entities">
        ${i([this.entities,this._renderEmptySortable],()=>this._renderEmptySortable?"":this.entities.map((entityConf,index)=>$`
                  <div class="entity" data-entity-id=${entityConf.entity}>
                    <ha-svg-icon .path=${mdiDrag}></ha-svg-icon>
                    <ha-entity-picker
                      .hass=${this.hass}
                      .value=${entityConf.entity}
                      .index=${index}
                      @value-changed=${this._valueChanged}
                      .includeDomains=${includeDomainsEntityPicker}
                      allow-custom-entity
                    ></ha-entity-picker>
                  </div>
                `))}
      </div>
      <ha-entity-picker
        class="add-entity"
        .hass=${this.hass}
        @value-changed=${this._addEntity}
        .includeDomains=${includeDomainsEntityPicker}
      ></ha-entity-picker>
    `;}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiEntityEditor.prototype),"updated",this).call(this,changedProps);const attachedChanged=changedProps.has("_attached");const entitiesChanged=changedProps.has("entities");if(!entitiesChanged&&!attachedChanged){return;}if(attachedChanged&&!this._attached){var _this$_sortable;// Tear down sortable, if available
(_this$_sortable=this._sortable)===null||_this$_sortable===void 0?void 0:_this$_sortable.destroy();this._sortable=undefined;return;}if(!this._sortable&&this.entities){this._createSortable();return;}if(entitiesChanged){this._handleEntitiesChanged();}}},{kind:"method",key:"_handleEntitiesChanged",value:async function _handleEntitiesChanged(){this._renderEmptySortable=true;await this.updateComplete;const container=this.shadowRoot.querySelector(".entities");while(container.lastElementChild){container.removeChild(container.lastElementChild);}this._renderEmptySortable=false;}},{kind:"method",key:"_createSortable",value:async function _createSortable(){if(!Sortable){const sortableImport=await import('./sortable.core.esm-dev.js');Sortable=sortableImport.Sortable;Sortable.mount(sortableImport.OnSpill);Sortable.mount(sortableImport.AutoScroll());}this._sortable=new Sortable(this.shadowRoot.querySelector(".entities"),{animation:150,fallbackClass:"sortable-fallback",handle:"ha-svg-icon",dataIdAttr:"data-entity-id",onEnd:async evt=>this._entityMoved(evt)});}},{kind:"method",key:"_addEntity",value:async function _addEntity(ev){const value=ev.detail.value;if(value===""){return;}const newConfigEntities=this.entities.concat({entity:value});ev.target.value="";fireEvent(this,"entities-changed",{entities:newConfigEntities});}},{kind:"method",key:"_entityMoved",value:function _entityMoved(ev){if(ev.oldIndex===ev.newIndex){return;}const newEntities=this.entities.concat();newEntities.splice(ev.newIndex,0,newEntities.splice(ev.oldIndex,1)[0]);fireEvent(this,"entities-changed",{entities:newEntities});}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const value=ev.detail.value;const index=ev.target.index;const newConfigEntities=this.entities.concat();if(value===""||value===undefined){newConfigEntities.splice(index,1);}else {newConfigEntities[index]={...newConfigEntities[index],entity:value};}fireEvent(this,"entities-changed",{entities:newConfigEntities});}},{kind:"get",static:true,key:"styles",value:function styles(){return [sortableStyles,r`
        ha-entity-picker {
          margin-top: 8px;
        }
        .add-entity {
          display: block;
          margin-left: 31px;
        }
        .entity {
          display: flex;
          align-items: center;
        }
        .entity ha-svg-icon {
          padding-right: 8px;
          cursor: move;
        }
        .entity ha-entity-picker {
          flex-grow: 1;
        }
      `];}}]};},s);
