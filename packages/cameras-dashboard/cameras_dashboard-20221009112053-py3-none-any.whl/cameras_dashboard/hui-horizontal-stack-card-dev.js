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

class HuiHorizontalStackCard extends HuiStackCard{async getCardSize(){if(!this._cards){return 0;}const promises=[];for(const element of this._cards){promises.push(computeCardSize(element));}const results=await Promise.all(promises);return Math.max(...results);}static get styles(){return [super.sharedStyles,r`
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
      `];}}customElements.define("hui-horizontal-stack-card",HuiHorizontalStackCard);
