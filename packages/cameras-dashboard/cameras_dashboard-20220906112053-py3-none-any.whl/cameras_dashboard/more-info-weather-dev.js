const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, bb as mdiThermometer, aq as mdiGauge, an as mdiWaterPercent, ap as mdiWeatherWindy, b5 as mdiEye, r, n, cM as mdiWeatherNight, bc as mdiWeatherCloudy, ao as mdiAlertCircleOutline, ar as mdiWeatherFog, e6 as mdiWeatherHail, e7 as mdiWeatherLightning, e8 as mdiWeatherLightningRainy, e9 as mdiWeatherPartlyCloudy, ea as mdiWeatherPouring, as as mdiWeatherRainy, eb as mdiWeatherSnowy, ec as mdiWeatherSnowyRainy, ed as mdiWeatherSunny, ee as mdiWeatherWindyVariant } from './main-dev.js';
import { f as formatNumber, ak as formatDateWeekday } from './auth-dev.js';
import { y as isForecastHourly, z as getWeatherUnit, A as getWind, B as formatTimeWeekday } from './ha-more-info-dialog-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

const weatherIcons={"clear-night":mdiWeatherNight,cloudy:mdiWeatherCloudy,exceptional:mdiAlertCircleOutline,fog:mdiWeatherFog,hail:mdiWeatherHail,lightning:mdiWeatherLightning,"lightning-rainy":mdiWeatherLightningRainy,partlycloudy:mdiWeatherPartlyCloudy,pouring:mdiWeatherPouring,rainy:mdiWeatherRainy,snowy:mdiWeatherSnowy,"snowy-rainy":mdiWeatherSnowyRainy,sunny:mdiWeatherSunny,windy:mdiWeatherWindy,"windy-variant":mdiWeatherWindyVariant};_decorate([n("more-info-weather")],function(_initialize,_LitElement){class MoreInfoWeather extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoWeather,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"method",key:"shouldUpdate",value:function shouldUpdate(changedProps){if(changedProps.has("stateObj")){return true;}const oldHass=changedProps.get("hass");if(!oldHass||oldHass.locale!==this.hass.locale||oldHass.config.unit_system!==this.hass.config.unit_system){return true;}return false;}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.stateObj){return $``;}const hourly=isForecastHourly(this.stateObj.attributes.forecast);return $`
      <div class="flex">
        <ha-svg-icon .path=${mdiThermometer}></ha-svg-icon>
        <div class="main">
          ${this.hass.localize("ui.card.weather.attributes.temperature")}
        </div>
        <div>
          ${formatNumber(this.stateObj.attributes.temperature,this.hass.locale)}
          ${getWeatherUnit(this.hass,"temperature")}
        </div>
      </div>
      ${this._showValue(this.stateObj.attributes.pressure)?$`
            <div class="flex">
              <ha-svg-icon .path=${mdiGauge}></ha-svg-icon>
              <div class="main">
                ${this.hass.localize("ui.card.weather.attributes.air_pressure")}
              </div>
              <div>
                ${formatNumber(this.stateObj.attributes.pressure,this.hass.locale)}
                ${getWeatherUnit(this.hass,"pressure")}
              </div>
            </div>
          `:""}
      ${this._showValue(this.stateObj.attributes.humidity)?$`
            <div class="flex">
              <ha-svg-icon .path=${mdiWaterPercent}></ha-svg-icon>
              <div class="main">
                ${this.hass.localize("ui.card.weather.attributes.humidity")}
              </div>
              <div>
                ${formatNumber(this.stateObj.attributes.humidity,this.hass.locale)}
                %
              </div>
            </div>
          `:""}
      ${this._showValue(this.stateObj.attributes.wind_speed)?$`
            <div class="flex">
              <ha-svg-icon .path=${mdiWeatherWindy}></ha-svg-icon>
              <div class="main">
                ${this.hass.localize("ui.card.weather.attributes.wind_speed")}
              </div>
              <div>
                ${getWind(this.hass,this.stateObj.attributes.wind_speed,this.stateObj.attributes.wind_bearing)}
              </div>
            </div>
          `:""}
      ${this._showValue(this.stateObj.attributes.visibility)?$`
            <div class="flex">
              <ha-svg-icon .path=${mdiEye}></ha-svg-icon>
              <div class="main">
                ${this.hass.localize("ui.card.weather.attributes.visibility")}
              </div>
              <div>
                ${formatNumber(this.stateObj.attributes.visibility,this.hass.locale)}
                ${getWeatherUnit(this.hass,"length")}
              </div>
            </div>
          `:""}
      ${this.stateObj.attributes.forecast?$`
            <div class="section">
              ${this.hass.localize("ui.card.weather.forecast")}:
            </div>
            ${this.stateObj.attributes.forecast.map(item=>this._showValue(item.templow)||this._showValue(item.temperature)?$`<div class="flex">
                    ${item.condition?$`
                          <ha-svg-icon
                            .path=${weatherIcons[item.condition]}
                          ></ha-svg-icon>
                        `:""}
                    ${hourly?$`
                          <div class="main">
                            ${formatTimeWeekday(new Date(item.datetime),this.hass.locale)}
                          </div>
                        `:$`
                          <div class="main">
                            ${formatDateWeekday(new Date(item.datetime),this.hass.locale)}
                          </div>
                        `}
                    <div class="templow">
                      ${this._showValue(item.templow)?`${formatNumber(item.templow,this.hass.locale)}
                          ${getWeatherUnit(this.hass,"temperature")}`:hourly?"":"—"}
                    </div>
                    <div class="temp">
                      ${this._showValue(item.temperature)?`${formatNumber(item.temperature,this.hass.locale)}
                        ${getWeatherUnit(this.hass,"temperature")}`:"—"}
                    </div>
                  </div>`:"")}
          `:""}
      ${this.stateObj.attributes.attribution?$`
            <div class="attribution">
              ${this.stateObj.attributes.attribution}
            </div>
          `:""}
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-svg-icon {
        color: var(--paper-item-icon-color);
      }
      .section {
        margin: 16px 0 8px 0;
        font-size: 1.2em;
      }

      .flex {
        display: flex;
        height: 32px;
        align-items: center;
      }

      .main {
        flex: 1;
        margin-left: 24px;
      }

      .temp,
      .templow {
        min-width: 48px;
        text-align: right;
      }

      .templow {
        margin: 0 16px;
        color: var(--secondary-text-color);
      }

      .attribution {
        color: var(--secondary-text-color);
        text-align: center;
      }
    `;}},{kind:"method",key:"_showValue",value:function _showValue(item){return typeof item!=="undefined"&&item!==null;}}]};},s);
