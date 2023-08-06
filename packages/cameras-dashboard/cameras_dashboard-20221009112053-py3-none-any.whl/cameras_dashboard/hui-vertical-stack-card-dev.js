const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { r } from './main-dev.js';
import { ao as HuiStackCard, aa as computeCardSize } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

class HuiVerticalStackCard extends HuiStackCard{async getCardSize(){if(!this._cards){return 0;}const promises=[];for(const element of this._cards){promises.push(computeCardSize(element));}const results=await Promise.all(promises);return results.reduce((partial_sum,a)=>partial_sum+a,0);}static get styles(){return [super.sharedStyles,r`
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
      `];}}customElements.define("hui-vertical-stack-card",HuiVerticalStackCard);
