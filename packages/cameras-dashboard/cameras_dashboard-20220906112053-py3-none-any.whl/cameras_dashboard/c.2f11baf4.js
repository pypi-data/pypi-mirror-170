import{eT as e,aS as a,eU as i,_ as t,c as o,d as n,t as s,f as d,$ as c,ax as r,r as l,n as h}from"./main-d07cb663.js";import{b as p}from"./c.c11921c6.js";import{G as m}from"./c.37525831.js";import"./c.62305b3f.js";import"./c.fc0bbf07.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";const g=[{type:"graph",icon:e},{type:"buttons",icon:a},{type:"picture",icon:i}];let u=t([h("hui-dialog-create-headerfooter")],(function(e,a){return{F:class extends a{constructor(...a){super(...a),e(this)}},d:[{kind:"field",decorators:[n({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[s()],key:"_params",value:void 0},{kind:"method",key:"showDialog",value:async function(e){this._params=e}},{kind:"method",key:"closeDialog",value:function(){return this._params=void 0,d(this,"dialog-closed",{dialog:this.localName}),!0}},{kind:"method",key:"render",value:function(){return this._params?c`
      <ha-dialog
        open
        scrimClickAction
        .heading=${p(this.hass,this.hass.localize("ui.panel.lovelace.editor.header-footer.choose_header_footer","type",this.hass.localize(`ui.panel.lovelace.editor.header-footer.${this._params.type}`)))}
        @keydown=${this._ignoreKeydown}
        @closed=${this._cancel}
      >
        <div class="elements">
          ${g.map(((e,a)=>c`
                <ha-card
                  role="button"
                  tabindex="0"
                  aria-labeledby=${"card-name-"+a}
                  outlined
                  .type=${e.type}
                  @click=${this._handleHeaderFooterPicked}
                  @keyDown=${this._handleHeaderFooterPicked}
                  dialogInitialFocus
                >
                  <ha-svg-icon .path=${e.icon}></ha-svg-icon>
                  <div .id=${"card-name-"+a} role="none presentation">
                    ${this.hass.localize(`ui.panel.lovelace.editor.header-footer.types.${e.type}.name`)}
                  </div>
                </ha-card>
              `))}
        </div>
        <div slot="primaryAction">
          <mwc-button @click=${this._cancel}>
            ${this.hass.localize("ui.common.cancel")}
          </mwc-button>
        </div>
      </ha-dialog>
    `:c``}},{kind:"method",key:"_handleHeaderFooterPicked",value:async function(e){if(e instanceof KeyboardEvent&&"Enter"!==e.key&&" "!==e.key&&"Spacebar"!==e.key)return;const a=e.currentTarget.type;let i={type:a};var t;this.hass&&(i=await(async(e,a,i,t)=>{let o={type:a};const n=await m(a);if(n&&n.getStubConfig){const a=await n.getStubConfig(e,i,t);o={...o,...a}}return o})(this.hass,a,(null===(t=this._params)||void 0===t?void 0:t.entities)||[],[]));this._params.pickHeaderFooter(i),this.closeDialog()}},{kind:"method",key:"_ignoreKeydown",value:function(e){e.stopPropagation()}},{kind:"method",key:"_cancel",value:function(e){e&&e.stopPropagation(),this.closeDialog()}},{kind:"get",static:!0,key:"styles",value:function(){return[r,l`
        @media all and (max-width: 450px), all and (max-height: 500px) {
          /* overrule the ha-style-dialog max-height on small screens */
          ha-dialog {
            --mdc-dialog-max-height: 100%;
            height: 100%;
          }
        }

        @media all and (min-width: 850px) {
          ha-dialog {
            --mdc-dialog-min-width: 550px;
          }
        }

        ha-dialog {
          --mdc-dialog-max-width: 550px;
          --dialog-content-padding: 2px 24px 20px 24px;
          --dialog-z-index: 5;
        }

        .elements {
          display: flex;
          flex-wrap: wrap;
        }

        .spinner,
        ha-card {
          width: calc(50% - 8px);
          text-align: center;
          margin: 4px;
        }

        ha-card {
          box-sizing: border-box;
          padding: 8px;
          color: var(--secondary-text-color);
          font-size: 16px;
          cursor: pointer;
        }

        ha-svg-icon {
          padding-bottom: 4px;
          --mdc-icon-size: 38px;
        }
      `]}}]}}),o);export{u as HuiCreateDialogHeaderFooter};
