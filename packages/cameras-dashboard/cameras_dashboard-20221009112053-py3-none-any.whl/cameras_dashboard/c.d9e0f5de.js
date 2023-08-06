import{_ as e,c as r,d as a,t,$ as i,eA as o,eB as s,ak as c,af as n,eC as l,eq as d,es as h,z as g,bM as v,eD as p,ca as y,c8 as f,r as m,n as u}from"./main-d07cb663.js";import{f as b}from"./c.fc0bbf07.js";import{g as k,e as $,b as x}from"./c.db8c8161.js";import{ac as _}from"./c.37525831.js";import{S as w}from"./c.65b9d701.js";import"./c.95ef015c.js";import"./c.c13d4687.js";import"./c.da136530.js";import"./c.655d6539.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";e([u("hui-energy-distribution-card")],(function(e,r){return{F:class extends r{constructor(...r){super(...r),e(this)}},d:[{kind:"field",decorators:[a({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_data",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:()=>["_config"]},{kind:"method",key:"setConfig",value:function(e){this._config=e}},{kind:"method",key:"hassSubscribe",value:function(){var e;return[k(this.hass,{key:null===(e=this._config)||void 0===e?void 0:e.collection_key}).subscribe((e=>{this._data=e}))]}},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"render",value:function(){var e,r;if(!this._config)return i``;if(!this._data)return i`${this.hass.localize("ui.panel.lovelace.cards.energy.loading")}`;const a=this._data.prefs,t=$(a),m=void 0!==t.solar,u=void 0!==t.battery,k=void 0!==t.gas,w=t.grid[0].flow_to.length>0,M=null!==(e=_(this._data.stats,t.grid[0].flow_from.map((e=>e.stat_energy_from))))&&void 0!==e?e:0;let j=null;var z;k&&(j=null!==(z=_(this._data.stats,t.gas.map((e=>e.stat_energy_from))))&&void 0!==z?z:0);let C=null;m&&(C=_(this._data.stats,t.solar.map((e=>e.stat_energy_from)))||0);let D=null,F=null;u&&(D=_(this._data.stats,t.battery.map((e=>e.stat_energy_to)))||0,F=_(this._data.stats,t.battery.map((e=>e.stat_energy_from)))||0);let W=null;w&&(W=_(this._data.stats,t.grid[0].flow_to.map((e=>e.stat_energy_to)))||0);let P=null;m&&(P=(C||0)-(W||0)-(D||0));let S=null,B=null;null!==P&&P<0&&(u&&(S=-1*P,S>M&&(B=Math.min(0,S-M),S=M)),P=0);let E=null;m&&u?(B||(B=Math.max(0,(W||0)-(C||0)-(D||0)-(S||0))),E=D-(S||0)):!m&&u&&(B=W);let q=null;u&&(q=(F||0)-(B||0));const A=Math.max(0,M-(S||0)),H=Math.max(0,A+(P||0)+(q||0));let R,O,T,V,Y;m&&(R=P/H*238.76104),q&&(O=q/H*238.76104);let G="https://app.electricitymap.org";if(this._data.co2SignalEntity&&this._data.fossilEnergyConsumption){const e=Object.values(this._data.fossilEnergyConsumption).reduce(((e,r)=>e+r),0),r=this.hass.states[this._data.co2SignalEntity];if(null!=r&&r.attributes.country_code&&(G+=`/zone/${r.attributes.country_code}`),null!==e){let r;T=M-e,r=A!==M?e*(A/M):e,Y=r/H*238.76104,V=238.76104-(R||0)-(O||0)-Y}}const I=A+(P||0)+(W?W-(B||0):0)+(E||0)+(q||0)+(S||0)+(B||0);return i`
      <ha-card .header=${this._config.title}>
        <div class="card-content">
          ${void 0!==T||m||k?i`<div class="row">
                ${void 0===T?i`<div class="spacer"></div>`:i`<div class="circle-container low-carbon">
                      <span class="label"
                        >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.non_fossil")}</span
                      >
                      <a
                        class="circle"
                        href=${G}
                        target="_blank"
                        rel="noopener no referrer"
                      >
                        <ha-svg-icon .path=${o}></ha-svg-icon>
                        ${T?b(T,this.hass.locale,{maximumFractionDigits:1}):"—"}
                        kWh
                      </a>
                      <svg width="80" height="30">
                        <line x1="40" y1="0" x2="40" y2="30"></line>
                      </svg>
                    </div>`}
                ${m?i`<div class="circle-container solar">
                      <span class="label"
                        >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.solar")}</span
                      >
                      <div class="circle">
                        <ha-svg-icon .path=${s}></ha-svg-icon>
                        ${b(C||0,this.hass.locale,{maximumFractionDigits:1})}
                        kWh
                      </div>
                    </div>`:k?i`<div class="spacer"></div>`:""}
                ${k?i`<div class="circle-container gas">
                      <span class="label"
                        >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.gas")}</span
                      >
                      <div class="circle">
                        <ha-svg-icon .path=${c}></ha-svg-icon>
                        ${b(j||0,this.hass.locale,{maximumFractionDigits:1})}
                        ${x(this.hass,a)||"m³"}
                      </div>
                      <svg width="80" height="30">
                        <path d="M40 0 v30" id="gas" />
                        ${j?n`<circle
                    r="1"
                    class="gas"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="2s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#gas" />
                    </animateMotion>
                  </circle>`:""}
                      </svg>
                    </div>`:i`<div class="spacer"></div>`}
              </div>`:""}
          <div class="row">
            <div class="circle-container grid">
              <div class="circle">
                <ha-svg-icon .path=${l}></ha-svg-icon>
                ${null!==W?i`<span class="return">
                      <ha-svg-icon
                        class="small"
                        .path=${d}
                      ></ha-svg-icon
                      >${b(W,this.hass.locale,{maximumFractionDigits:1})}
                      kWh
                    </span>`:""}
                <span class="consumption">
                  ${w?i`<ha-svg-icon
                        class="small"
                        .path=${h}
                      ></ha-svg-icon>`:""}${b(M,this.hass.locale,{maximumFractionDigits:1})}
                  kWh
                </span>
              </div>
              <span class="label"
                >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.grid")}</span
              >
            </div>
            <div class="circle-container home">
              <div
                class="circle ${g({border:void 0===R&&void 0===V})}"
              >
                <ha-svg-icon .path=${v}></ha-svg-icon>
                ${b(H,this.hass.locale,{maximumFractionDigits:1})}
                kWh
                ${void 0!==R||void 0!==V?i`<svg>
                      ${void 0!==R?n`<circle
                            class="solar"
                            cx="40"
                            cy="40"
                            r="38"
                            stroke-dasharray="${R} ${238.76104-R}"
                            shape-rendering="geometricPrecision"
                            stroke-dashoffset="-${238.76104-R}"
                          />`:""}
                      ${O?n`<circle
                            class="battery"
                            cx="40"
                            cy="40"
                            r="38"
                            stroke-dasharray="${O} ${238.76104-O}"
                            stroke-dashoffset="-${238.76104-O-(R||0)}"
                            shape-rendering="geometricPrecision"
                          />`:""}
                      ${V?n`<circle
                            class="low-carbon"
                            cx="40"
                            cy="40"
                            r="38"
                            stroke-dasharray="${V} ${238.76104-V}"
                            stroke-dashoffset="-${238.76104-V-(O||0)-(R||0)}"
                            shape-rendering="geometricPrecision"
                          />`:""}
                      <circle
                        class="grid"
                        cx="40"
                        cy="40"
                        r="38"
                        stroke-dasharray="${null!==(r=Y)&&void 0!==r?r:238.76104-R-(O||0)} ${void 0!==Y?238.76104-Y:R+(O||0)}"
                        stroke-dashoffset="0"
                        shape-rendering="geometricPrecision"
                      />
                    </svg>`:""}
              </div>
              <span class="label"
                >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.home")}</span
              >
            </div>
          </div>
          ${u?i`<div class="row">
                <div class="spacer"></div>
                <div class="circle-container battery">
                  <div class="circle">
                    <ha-svg-icon .path=${p}></ha-svg-icon>
                    <span class="battery-in">
                      <ha-svg-icon
                        class="small"
                        .path=${y}
                      ></ha-svg-icon
                      >${b(D||0,this.hass.locale,{maximumFractionDigits:1})}
                      kWh</span
                    >
                    <span class="battery-out">
                      <ha-svg-icon
                        class="small"
                        .path=${f}
                      ></ha-svg-icon>
                      ${b(F||0,this.hass.locale,{maximumFractionDigits:1})}
                      kWh</span
                    >
                  </div>
                  <span class="label"
                    >${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.battery")}</span
                  >
                </div>
                <div class="spacer"></div>
              </div>`:""}
          <div class="lines ${g({battery:u})}">
            <svg
              viewBox="0 0 100 100"
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="xMidYMid slice"
            >
              ${w&&m?n`<path
                    id="return"
                    class="return"
                    d="M${u?45:47},0 v15 c0,${u?"35 -10,30 -30,30":"40 -10,35 -30,35"} h-20"
                    vector-effect="non-scaling-stroke"
                  ></path> `:""}
              ${m?n`<path
                    id="solar"
                    class="solar"
                    d="M${u?55:53},0 v15 c0,${u?"35 10,30 30,30":"40 10,35 30,35"} h20"
                    vector-effect="non-scaling-stroke"
                  ></path>`:""}
              ${u?n`<path
                    id="battery-house"
                    class="battery-house"
                    d="M55,100 v-15 c0,-35 10,-30 30,-30 h20"
                    vector-effect="non-scaling-stroke"
                  ></path>
                  <path
                    id="battery-grid"
                    class=${g({"battery-from-grid":Boolean(S),"battery-to-grid":Boolean(B)})}
                    d="M45,100 v-15 c0,-35 -10,-30 -30,-30 h-20"
                    vector-effect="non-scaling-stroke"
                  ></path>
                  `:""}
              ${u&&m?n`<path
                    id="battery-solar"
                    class="battery-solar"
                    d="M50,0 V100"
                    vector-effect="non-scaling-stroke"
                  ></path>`:""}
              <path
                class="grid"
                id="grid"
                d="M0,${u?50:m?56:53} H100"
                vector-effect="non-scaling-stroke"
              ></path>
              ${W&&m?n`<circle
                    r="1"
                    class="return"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-(W-(B||0))/I*6}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#return" />
                    </animateMotion>
                  </circle>`:""}
              ${P?n`<circle
                    r="1"
                    class="solar"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-P/I*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#solar" />
                    </animateMotion>
                  </circle>`:""}
              ${A?n`<circle
                    r="1"
                    class="grid"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-A/I*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#grid" />
                    </animateMotion>
                  </circle>`:""}
              ${E?n`<circle
                    r="1"
                    class="battery-solar"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-E/I*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-solar" />
                    </animateMotion>
                  </circle>`:""}
              ${q?n`<circle
                    r="1"
                    class="battery-house"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-q/I*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-house" />
                    </animateMotion>
                  </circle>`:""}
              ${S?n`<circle
                    r="1"
                    class="battery-from-grid"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-S/I*5}s"
                      repeatCount="indefinite"
                      keyPoints="1;0" keyTimes="0;1"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-grid" />
                    </animateMotion>
                  </circle>`:""}
              ${B?n`<circle
                    r="1"
                    class="battery-to-grid"
                    vector-effect="non-scaling-stroke"
                  >
                    <animateMotion
                      dur="${6-B/I*5}s"
                      repeatCount="indefinite"
                      calcMode="linear"
                    >
                      <mpath xlink:href="#battery-grid" />
                    </animateMotion>
                  </circle>`:""}
            </svg>
          </div>
        </div>
        ${this._config.link_dashboard?i`
              <div class="card-actions">
                <a href="/energy"
                  ><mwc-button>
                    ${this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.go_to_energy_dashboard")}
                  </mwc-button></a
                >
              </div>
            `:""}
      </ha-card>
    `}},{kind:"field",static:!0,key:"styles",value:()=>m`
    :host {
      --mdc-icon-size: 24px;
    }
    .card-content {
      position: relative;
    }
    .lines {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 146px;
      display: flex;
      justify-content: center;
      padding: 0 16px 16px;
      box-sizing: border-box;
    }
    .lines.battery {
      bottom: 100px;
      height: 156px;
    }
    .lines svg {
      width: calc(100% - 160px);
      height: 100%;
      max-width: 340px;
    }
    .row {
      display: flex;
      justify-content: space-between;
      max-width: 500px;
      margin: 0 auto;
    }
    .circle-container {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .circle-container.low-carbon {
      margin-right: 4px;
    }
    .circle-container.solar {
      margin: 0 4px;
      height: 130px;
    }
    .circle-container.gas {
      margin-left: 4px;
      height: 130px;
    }
    .circle-container.battery {
      height: 110px;
      justify-content: flex-end;
    }
    .spacer {
      width: 84px;
    }
    .circle {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      box-sizing: border-box;
      border: 2px solid;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      font-size: 12px;
      line-height: 12px;
      position: relative;
      text-decoration: none;
      color: var(--primary-text-color);
    }
    ha-svg-icon {
      padding-bottom: 2px;
    }
    ha-svg-icon.small {
      --mdc-icon-size: 12px;
    }
    .label {
      color: var(--secondary-text-color);
      font-size: 12px;
    }
    line,
    path {
      stroke: var(--primary-text-color);
      stroke-width: 1;
      fill: none;
    }
    .circle svg {
      position: absolute;
      fill: none;
      stroke-width: 4px;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
    }
    .gas path,
    .gas circle {
      stroke: var(--energy-gas-color);
    }
    circle.gas {
      stroke-width: 4;
      fill: var(--energy-gas-color);
    }
    .gas .circle {
      border-color: var(--energy-gas-color);
    }
    .low-carbon line {
      stroke: var(--energy-non-fossil-color);
    }
    .low-carbon .circle {
      border-color: var(--energy-non-fossil-color);
    }
    .low-carbon ha-svg-icon {
      color: var(--energy-non-fossil-color);
    }
    circle.low-carbon {
      stroke: var(--energy-non-fossil-color);
      fill: var(--energy-non-fossil-color);
    }
    .solar .circle {
      border-color: var(--energy-solar-color);
    }
    circle.solar,
    path.solar {
      stroke: var(--energy-solar-color);
    }
    circle.solar {
      stroke-width: 4;
      fill: var(--energy-solar-color);
    }
    .battery .circle {
      border-color: var(--energy-battery-in-color);
    }
    circle.battery,
    path.battery {
      stroke: var(--energy-battery-out-color);
    }
    path.battery-house,
    circle.battery-house {
      stroke: var(--energy-battery-out-color);
    }
    circle.battery-house {
      stroke-width: 4;
      fill: var(--energy-battery-out-color);
    }
    path.battery-solar,
    circle.battery-solar {
      stroke: var(--energy-battery-in-color);
    }
    circle.battery-solar {
      stroke-width: 4;
      fill: var(--energy-battery-in-color);
    }
    .battery-in {
      color: var(--energy-battery-in-color);
    }
    .battery-out {
      color: var(--energy-battery-out-color);
    }
    path.battery-from-grid {
      stroke: var(--energy-grid-consumption-color);
    }
    path.battery-to-grid {
      stroke: var(--energy-grid-return-color);
    }
    path.return,
    circle.return,
    circle.battery-to-grid {
      stroke: var(--energy-grid-return-color);
    }
    circle.return,
    circle.battery-to-grid {
      stroke-width: 4;
      fill: var(--energy-grid-return-color);
    }
    .return {
      color: var(--energy-grid-return-color);
    }
    .grid .circle {
      border-color: var(--energy-grid-consumption-color);
    }
    .consumption {
      color: var(--energy-grid-consumption-color);
    }
    circle.grid,
    circle.battery-from-grid,
    path.grid {
      stroke: var(--energy-grid-consumption-color);
    }
    circle.grid,
    circle.battery-from-grid {
      stroke-width: 4;
      fill: var(--energy-grid-consumption-color);
    }
    .home .circle {
      border-width: 0;
      border-color: var(--primary-color);
    }
    .home .circle.border {
      border-width: 2px;
    }
    .circle svg circle {
      animation: rotate-in 0.6s ease-in;
      transition: stroke-dashoffset 0.4s, stroke-dasharray 0.4s;
      fill: none;
    }
    @keyframes rotate-in {
      from {
        stroke-dashoffset: 238.76104;
        stroke-dasharray: 238.76104;
      }
    }
    .card-actions a {
      text-decoration: none;
    }
  `}]}}),w(r));
