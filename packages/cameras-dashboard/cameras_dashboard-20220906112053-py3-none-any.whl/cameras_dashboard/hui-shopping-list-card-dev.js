const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, G as i, j as _get, k as _getPrototypeOf, S as applyThemesOnElement, $, z as o, dF as mdiPlus, eN as mdiSort, eO as mdiNotificationClearAll, ep as mdiDrag, r, n } from './main-dev.js';
import { i as i$1 } from './guard-dev.js';
import { c } from './repeat-dev.js';
import './ha-checkbox-dev.js';
import { S as SubscribeMixin } from './subscribe-mixin-dev.js';
import './mwc-checkbox.css-dev.js';

const fetchItems=hass=>hass.callWS({type:"shopping_list/items"});const updateItem=(hass,itemId,item)=>hass.callWS({type:"shopping_list/items/update",item_id:itemId,...item});const clearItems=hass=>hass.callWS({type:"shopping_list/items/clear"});const addItem=(hass,name)=>hass.callWS({type:"shopping_list/items/add",name});const reorderItems=(hass,itemIds)=>hass.callWS({type:"shopping_list/items/reorder",item_ids:itemIds});

let Sortable;_decorate([n("hui-shopping-list-card")],function(_initialize,_SubscribeMixin){class HuiShoppingListCard extends _SubscribeMixin{constructor(...args){super(...args);_initialize(this);}}return {F:HuiShoppingListCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-shopping-list-editor-dev.js');return document.createElement("hui-shopping-list-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(){return {type:"shopping-list"};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_uncheckedItems",value:void 0},{kind:"field",decorators:[t()],key:"_checkedItems",value:void 0},{kind:"field",decorators:[t()],key:"_reordering",value(){return false;}},{kind:"field",decorators:[t()],key:"_renderEmptySortable",value(){return false;}},{kind:"field",key:"_sortable",value:void 0},{kind:"field",decorators:[i("#sortable")],key:"_sortableEl",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return (this._config?this._config.title?2:0:0)+3;}},{kind:"method",key:"setConfig",value:function setConfig(config){this._config=config;this._uncheckedItems=[];this._checkedItems=[];}},{kind:"method",key:"hassSubscribe",value:function hassSubscribe(){this._fetchData();return [this.hass.connection.subscribeEvents(()=>this._fetchData(),"shopping_list_updated")];}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiShoppingListCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass){return;}const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(changedProps.has("hass")&&(oldHass===null||oldHass===void 0?void 0:oldHass.themes)!==this.hass.themes||changedProps.has("_config")&&(oldConfig===null||oldConfig===void 0?void 0:oldConfig.theme)!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}}},{kind:"method",key:"render",value:function render(){if(!this._config||!this.hass){return $``;}return $`
      <ha-card
        .header=${this._config.title}
        class=${o({"has-header":"title"in this._config})}
      >
        <div class="addRow">
          <ha-svg-icon
            class="addButton"
            .path=${mdiPlus}
            .title=${this.hass.localize("ui.panel.lovelace.cards.shopping-list.add_item")}
            @click=${this._addItem}
          >
          </ha-svg-icon>
          <ha-textfield
            class="addBox"
            .placeholder=${this.hass.localize("ui.panel.lovelace.cards.shopping-list.add_item")}
            @keydown=${this._addKeyPress}
          ></ha-textfield>
          <ha-svg-icon
            class="reorderButton"
            .path=${mdiSort}
            .title=${this.hass.localize("ui.panel.lovelace.cards.shopping-list.reorder_items")}
            @click=${this._toggleReorder}
          >
          </ha-svg-icon>
        </div>
        ${this._reordering?$`
              <div id="sortable">
                ${i$1([this._uncheckedItems,this._renderEmptySortable],()=>this._renderEmptySortable?"":this._renderItems(this._uncheckedItems))}
              </div>
            `:this._renderItems(this._uncheckedItems)}
        ${this._checkedItems.length>0?$`
              <div class="divider"></div>
              <div class="checked">
                <span>
                  ${this.hass.localize("ui.panel.lovelace.cards.shopping-list.checked_items")}
                </span>
                <ha-svg-icon
                  class="clearall"
                  tabindex="0"
                  .path=${mdiNotificationClearAll}
                  .title=${this.hass.localize("ui.panel.lovelace.cards.shopping-list.clear_items")}
                  @click=${this._clearItems}
                >
                </ha-svg-icon>
              </div>
              ${c(this._checkedItems,item=>item.id,item=>$`
                    <div class="editRow">
                      <ha-checkbox
                        tabindex="0"
                        .checked=${item.complete}
                        .itemId=${item.id}
                        @change=${this._completeItem}
                      ></ha-checkbox>
                      <ha-textfield
                        class="item"
                        .value=${item.name}
                        .itemId=${item.id}
                        @change=${this._saveEdit}
                      ></ha-textfield>
                    </div>
                  `)}
            `:""}
      </ha-card>
    `;}},{kind:"method",key:"_renderItems",value:function _renderItems(items){return $`
      ${c(items,item=>item.id,item=>$`
            <div class="editRow" item-id=${item.id}>
              <ha-checkbox
                tabindex="0"
                .checked=${item.complete}
                .itemId=${item.id}
                @change=${this._completeItem}
              ></ha-checkbox>
              <ha-textfield
                class="item"
                .value=${item.name}
                .itemId=${item.id}
                @change=${this._saveEdit}
              ></ha-textfield>
              ${this._reordering?$`
                    <ha-svg-icon
                      .title=${this.hass.localize("ui.panel.lovelace.cards.shopping-list.drag_and_drop")}
                      class="reorderButton"
                      .path=${mdiDrag}
                    >
                    </ha-svg-icon>
                  `:""}
            </div>
          `)}
    `;}},{kind:"method",key:"_fetchData",value:async function _fetchData(){if(!this.hass){return;}const checkedItems=[];const uncheckedItems=[];const items=await fetchItems(this.hass);for(const key in items){if(items[key].complete){checkedItems.push(items[key]);}else {uncheckedItems.push(items[key]);}}this._checkedItems=checkedItems;this._uncheckedItems=uncheckedItems;}},{kind:"method",key:"_completeItem",value:function _completeItem(ev){updateItem(this.hass,ev.target.itemId,{complete:ev.target.checked}).catch(()=>this._fetchData());}},{kind:"method",key:"_saveEdit",value:function _saveEdit(ev){updateItem(this.hass,ev.target.itemId,{name:ev.target.value}).catch(()=>this._fetchData());ev.target.blur();}},{kind:"method",key:"_clearItems",value:function _clearItems(){if(this.hass){clearItems(this.hass).catch(()=>this._fetchData());}}},{kind:"get",key:"_newItem",value:function _newItem(){return this.shadowRoot.querySelector(".addBox");}},{kind:"method",key:"_addItem",value:function _addItem(ev){const newItem=this._newItem;if(newItem.value.length>0){addItem(this.hass,newItem.value).catch(()=>this._fetchData());}newItem.value="";if(ev){newItem.focus();}}},{kind:"method",key:"_addKeyPress",value:function _addKeyPress(ev){if(ev.keyCode===13){this._addItem(null);}}},{kind:"method",key:"_toggleReorder",value:async function _toggleReorder(){if(!Sortable){const sortableImport=await import('./sortable.core.esm-dev.js');Sortable=sortableImport.Sortable;}this._reordering=!this._reordering;await this.updateComplete;if(this._reordering){this._createSortable();}else {var _this$_sortable;(_this$_sortable=this._sortable)===null||_this$_sortable===void 0?void 0:_this$_sortable.destroy();this._sortable=undefined;}}},{kind:"method",key:"_createSortable",value:function _createSortable(){const sortableEl=this._sortableEl;this._sortable=new Sortable(sortableEl,{animation:150,fallbackClass:"sortable-fallback",dataIdAttr:"item-id",handle:"ha-svg-icon",onEnd:async evt=>{// Since this is `onEnd` event, it's possible that
// an item wa dragged away and was put back to its original position.
if(evt.oldIndex!==evt.newIndex){reorderItems(this.hass,this._sortable.toArray()).catch(()=>this._fetchData());// Move the shopping list item in memory.
this._uncheckedItems.splice(evt.newIndex,0,this._uncheckedItems.splice(evt.oldIndex,1)[0]);}this._renderEmptySortable=true;await this.updateComplete;while(sortableEl!==null&&sortableEl!==void 0&&sortableEl.lastElementChild){sortableEl.removeChild(sortableEl.lastElementChild);}this._renderEmptySortable=false;}});}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        padding: 16px;
        height: 100%;
        box-sizing: border-box;
      }

      .has-header {
        padding-top: 0;
      }

      .editRow,
      .addRow,
      .checked {
        display: flex;
        flex-direction: row;
        align-items: center;
      }

      .item {
        margin-top: 8px;
      }

      .addButton {
        padding-right: 16px;
        cursor: pointer;
      }

      .reorderButton {
        padding-left: 16px;
        cursor: pointer;
      }

      ha-checkbox {
        margin-left: -12px;
      }

      ha-textfield {
        flex-grow: 1;
      }

      .checked {
        margin: 12px 0;
        justify-content: space-between;
      }

      .checked span {
        color: var(--primary-text-color);
        font-weight: 500;
      }

      .divider {
        height: 1px;
        background-color: var(--divider-color);
        margin: 10px 0;
      }

      .clearall {
        cursor: pointer;
      }
    `;}}]};},SubscribeMixin(s));
