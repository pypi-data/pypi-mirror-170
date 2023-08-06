import{r}from"./main-d07cb663.js";import{ao as t,aa as s}from"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.fc0bbf07.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";customElements.define("hui-vertical-stack-card",class extends t{async getCardSize(){if(!this._cards)return 0;const r=[];for(const t of this._cards)r.push(s(t));return(await Promise.all(r)).reduce(((r,t)=>r+t),0)}static get styles(){return[super.sharedStyles,r`
        #root {
          display: flex;
          flex-direction: column;
          height: 100%;
        }
        #root > * {
          margin: var(
            --vertical-stack-card-margin,
            var(--stack-card-margin, 4px 0)
          );
        }
        #root > *:first-child {
          margin-top: 0;
        }
        #root > *:last-child {
          margin-bottom: 0;
        }
      `]}});
