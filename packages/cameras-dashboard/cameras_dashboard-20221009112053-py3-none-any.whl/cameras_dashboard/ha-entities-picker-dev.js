const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, f as fireEvent, r, n } from './main-dev.js';
import { D as isValidEntityId } from './ha-more-info-dialog-dev.js';
import './ha-entity-picker-dev.js';

_decorate([n("ha-entities-picker")],function(_initialize,_LitElement){class HaEntitiesPickerLight extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaEntitiesPickerLight,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({type:Array})],key:"value",value:void 0},{kind:"field",decorators:[e({type:Array,attribute:"include-domains"})],key:"includeDomains",value:void 0},{kind:"field",decorators:[e({type:Array,attribute:"exclude-domains"})],key:"excludeDomains",value:void 0},{kind:"field",decorators:[e({type:Array,attribute:"include-device-classes"})],key:"includeDeviceClasses",value:void 0},{kind:"field",decorators:[e({type:Array,attribute:"include-unit-of-measurement"})],key:"includeUnitOfMeasurement",value:void 0},{kind:"field",decorators:[e({attribute:"picked-entity-label"})],key:"pickedEntityLabel",value:void 0},{kind:"field",decorators:[e({attribute:"pick-entity-label"})],key:"pickEntityLabel",value:void 0},{kind:"method",key:"render",value:/**
   * Show entities from specific domains.
   * @type {string}
   * @attr include-domains
   */ /**
   * Show no entities of these domains.
   * @type {Array}
   * @attr exclude-domains
   */ /**
   * Show only entities of these device classes.
   * @type {Array}
   * @attr include-device-classes
   */ /**
   * Show only entities with these unit of measuments.
   * @type {Array}
   * @attr include-unit-of-measurement
   */function render(){if(!this.hass){return $``;}const currentEntities=this._currentEntities;return $`
      ${currentEntities.map(entityId=>$`
          <div>
            <ha-entity-picker
              allow-custom-entity
              .curValue=${entityId}
              .hass=${this.hass}
              .includeDomains=${this.includeDomains}
              .excludeDomains=${this.excludeDomains}
              .includeDeviceClasses=${this.includeDeviceClasses}
              .includeUnitOfMeasurement=${this.includeUnitOfMeasurement}
              .entityFilter=${this._entityFilter}
              .value=${entityId}
              .label=${this.pickedEntityLabel}
              @value-changed=${this._entityChanged}
            ></ha-entity-picker>
          </div>
        `)}
      <div>
        <ha-entity-picker
          .hass=${this.hass}
          .includeDomains=${this.includeDomains}
          .excludeDomains=${this.excludeDomains}
          .includeDeviceClasses=${this.includeDeviceClasses}
          .includeUnitOfMeasurement=${this.includeUnitOfMeasurement}
          .entityFilter=${this._entityFilter}
          .label=${this.pickEntityLabel}
          @value-changed=${this._addEntity}
        ></ha-entity-picker>
      </div>
    `;}},{kind:"field",key:"_entityFilter",value(){return stateObj=>!this.value||!this.value.includes(stateObj.entity_id);}},{kind:"get",key:"_currentEntities",value:function _currentEntities(){return this.value||[];}},{kind:"method",key:"_updateEntities",value:async function _updateEntities(entities){this.value=entities;fireEvent(this,"value-changed",{value:entities});}},{kind:"method",key:"_entityChanged",value:function _entityChanged(event){event.stopPropagation();const curValue=event.currentTarget.curValue;const newValue=event.detail.value;if(newValue===curValue||newValue!==undefined&&!isValidEntityId(newValue)){return;}const currentEntities=this._currentEntities;if(!newValue||currentEntities.includes(newValue)){this._updateEntities(currentEntities.filter(ent=>ent!==curValue));return;}this._updateEntities(currentEntities.map(ent=>ent===curValue?newValue:ent));}},{kind:"method",key:"_addEntity",value:async function _addEntity(event){event.stopPropagation();const toAdd=event.detail.value;if(!toAdd){return;}event.currentTarget.value="";if(!toAdd){return;}const currentEntities=this._currentEntities;if(currentEntities.includes(toAdd)){return;}this._updateEntities([...currentEntities,toAdd]);}},{kind:"field",static:true,key:"styles",value(){return r`
    div {
      margin-top: 8px;
    }
  `;}}]};},s);
