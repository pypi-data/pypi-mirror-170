import{r as t}from"./main-d07cb663.js";import{ao as r,aa as s}from"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.fc0bbf07.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";customElements.define("hui-horizontal-stack-card",class extends r{async getCardSize(){if(!this._cards)return 0;const t=[];for(const r of this._cards)t.push(s(r));const r=await Promise.all(t);return Math.max(...r)}static get styles(){return[super.sharedStyles,t`
        #root {
          display: flex;
          height: 100%;
        }
        #root > * {
          flex: 1 1 0;
          margin: var(
            --horizontal-stack-card-margin,
            var(--stack-card-margin, 0 4px)
          );
          min-width: 0;
        }
        #root > *:first-child {
          margin-left: 0;
        }
        #root > *:last-child {
          margin-right: 0;
        }
      `]}});
