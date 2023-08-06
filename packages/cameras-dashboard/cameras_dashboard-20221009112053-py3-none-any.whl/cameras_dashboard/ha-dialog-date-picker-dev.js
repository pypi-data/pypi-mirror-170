const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { $, r, eP as supportsPassiveEventListener, ah as __decorate, d as e, G as i, K as e$1, c as s, z as o, _ as _decorate, t, f as fireEvent, ax as haStyleDialog, n } from './main-dev.js';
import { d } from './ha-more-info-dialog-dev.js';
import { c } from './repeat-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';

const INTL_DATE_TIME_FORMAT=Intl&&Intl.DateTimeFormat;const UP_KEYS=[38,33,36];const DOWN_KEYS=[40,34,35];const PREV_KEY_CODES_SET=new Set([37,...UP_KEYS]);const NEXT_KEY_CODES_SET=new Set([39,...DOWN_KEYS]);const NEXT_DAY_KEY_CODES_SET=new Set([39,...UP_KEYS]);const PREV_DAY_KEY_CODES_SET=new Set([37,...DOWN_KEYS]);const ALL_NAV_KEYS_SET=new Set([37,39,...UP_KEYS,...DOWN_KEYS]);const DATEPICKER_NAME='app-datepicker';

function toUTCDate(y,m,d){return new Date(Date.UTC(y,m,d));}

const iconChevronLeft=$`<svg height="24" viewBox="0 0 24 24" width="24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"></path></svg>`;const iconChevronRight=$`<svg height="24" viewBox="0 0 24 24" width="24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg>`;

const resetButton=r`
button {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;

  position: relative;
  display: block;
  margin: 0;
  padding: 0;
  background: none; /** NOTE: IE11 fix */
  color: inherit;
  border: none;
  font: inherit;
  text-align: left;
  text-transform: inherit;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
`;r`
a {
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);

  position: relative;
  display: inline-block;
  background: initial;
  color: inherit;
  font: inherit;
  text-transform: inherit;
  text-decoration: none;
  outline: none;
}
a:focus,
a:focus.page-selected {
  text-decoration: underline;
}
`;r`
svg {
  display: block;
  min-width: var(--svg-icon-min-width, 24px);
  min-height: var(--svg-icon-min-height, 24px);
  fill: var(--svg-icon-fill, currentColor);
  pointer-events: none;
}
`;r`[hidden] { display: none !important; }`;const datepickerVariables=r`
:host {
  display: block;

  /* --app-datepicker-width: 300px; */
  /* --app-datepicker-primary-color: #4285f4; */
  /* --app-datepicker-header-height: 80px; */
}

* {
  box-sizing: border-box;
}
`;

async function animateElement(node,opts){const{hasNativeWebAnimation=false,keyframes=[],options={duration:100}}=opts||{};if(!Array.isArray(keyframes)||!keyframes.length)return;return new Promise(y=>{if(hasNativeWebAnimation){const animationEnd=node.animate(keyframes,options);animationEnd.onfinish=()=>y();}else {const[,endFrame]=keyframes||[];const transitionEnd=()=>{node.removeEventListener('transitionend',transitionEnd);y();};node.addEventListener('transitionend',transitionEnd);node.style.transitionDuration=`${options.duration}ms`;if(options.easing)node.style.transitionTimingFunction=options.easing;Object.keys(endFrame).forEach(n=>{if(n)node.style[n]=endFrame[n];});}});}

function getDateRange(min,max){return +max-+min;}

function getNextSelectableDate({keyCode,disabledDaysSet,disabledDatesSet,focusedDate,maxTime,minTime}){const focusedDateTime=+focusedDate;let isLessThanMinTime=focusedDateTime<minTime;let isMoreThanMaxTime=focusedDateTime>maxTime;if(getDateRange(minTime,maxTime)<864e5)return focusedDate;let isDisabledDay=isLessThanMinTime||isMoreThanMaxTime||disabledDaysSet.has(focusedDate.getUTCDay())||disabledDatesSet.has(focusedDateTime);if(!isDisabledDay)return focusedDate;let selectableFocusedDateTime=0;let selectableFocusedDate=isLessThanMinTime===isMoreThanMaxTime?focusedDate:new Date(isLessThanMinTime?minTime-864e5:864e5+maxTime);const fy=selectableFocusedDate.getUTCFullYear();const m=selectableFocusedDate.getUTCMonth();let d=selectableFocusedDate.getUTCDate();while(isDisabledDay){if(isLessThanMinTime||!isMoreThanMaxTime&&NEXT_DAY_KEY_CODES_SET.has(keyCode))d+=1;if(isMoreThanMaxTime||!isLessThanMinTime&&PREV_DAY_KEY_CODES_SET.has(keyCode))d-=1;selectableFocusedDate=toUTCDate(fy,m,d);selectableFocusedDateTime=+selectableFocusedDate;if(!isLessThanMinTime){isLessThanMinTime=selectableFocusedDateTime<minTime;if(isLessThanMinTime){selectableFocusedDate=new Date(minTime);selectableFocusedDateTime=+selectableFocusedDate;d=selectableFocusedDate.getUTCDate();}}if(!isMoreThanMaxTime){isMoreThanMaxTime=selectableFocusedDateTime>maxTime;if(isMoreThanMaxTime){selectableFocusedDate=new Date(maxTime);selectableFocusedDateTime=+selectableFocusedDate;d=selectableFocusedDate.getUTCDate();}}isDisabledDay=disabledDaysSet.has(selectableFocusedDate.getUTCDay())||disabledDatesSet.has(selectableFocusedDateTime);}return selectableFocusedDate;}

function computeNextFocusedDate({hasAltKey,keyCode,focusedDate,selectedDate,disabledDaysSet,disabledDatesSet,minTime,maxTime}){const oldFy=focusedDate.getUTCFullYear();const oldM=focusedDate.getUTCMonth();const oldD=focusedDate.getUTCDate();const focusedDateTime=+focusedDate;const sdFy=selectedDate.getUTCFullYear();const sdM=selectedDate.getUTCMonth();const notInCurrentMonth=sdM!==oldM||sdFy!==oldFy;let fy=oldFy;let m=oldM;let d=oldD;let shouldRunSwitch=true;if(notInCurrentMonth){fy=sdFy;m=sdM;d=1;shouldRunSwitch=keyCode===34||keyCode===33||keyCode===35;}switch(shouldRunSwitch){case focusedDateTime===minTime&&PREV_KEY_CODES_SET.has(keyCode):case focusedDateTime===maxTime&&NEXT_KEY_CODES_SET.has(keyCode):break;case keyCode===38:{d-=7;break;}case keyCode===40:{d+=7;break;}case keyCode===37:{d-=1;break;}case keyCode===39:{d+=1;break;}case keyCode===34:{hasAltKey?fy+=1:m+=1;break;}case keyCode===33:{hasAltKey?fy-=1:m-=1;break;}case keyCode===35:{m+=1;d=0;break;}case keyCode===36:default:{d=1;}}if(keyCode===34||keyCode===33){const totalDaysOfMonth=toUTCDate(fy,m+1,0).getUTCDate();if(d>totalDaysOfMonth){d=totalDaysOfMonth;}}const newFocusedDate=getNextSelectableDate({keyCode,maxTime,minTime,disabledDaysSet,disabledDatesSet,focusedDate:toUTCDate(fy,m,d)});return newFocusedDate;}

function dispatchCustomEvent(target,eventName,detail){return target.dispatchEvent(new CustomEvent(eventName,{detail,bubbles:true,composed:true}));}

function findShadowTarget(ev,callback){return ev.composedPath().find(n=>{if(n instanceof HTMLElement)return callback(n);return false;});}

function getFormatter(formatter){return n=>formatter.format(n).replace(/\u200e/gi,'');}

function getFormatters(locale){const dateFmt=INTL_DATE_TIME_FORMAT(locale,{timeZone:'UTC',weekday:'short',month:'short',day:'numeric'});const dayFmt=INTL_DATE_TIME_FORMAT(locale,{timeZone:'UTC',day:'numeric'});const fullDateFmt=INTL_DATE_TIME_FORMAT(locale,{timeZone:'UTC',year:'numeric',month:'short',day:'numeric'});const longMonthYearFmt=INTL_DATE_TIME_FORMAT(locale,{timeZone:'UTC',year:'numeric',month:'long'});const longWeekdayFmt=INTL_DATE_TIME_FORMAT(locale,{timeZone:'UTC',weekday:'long'});const narrowWeekdayFmt=INTL_DATE_TIME_FORMAT(locale,{timeZone:'UTC',weekday:'narrow'});const yearFmt=INTL_DATE_TIME_FORMAT(locale,{timeZone:'UTC',year:'numeric'});return {locale,dateFormat:getFormatter(dateFmt),dayFormat:getFormatter(dayFmt),fullDateFormat:getFormatter(fullDateFmt),longMonthYearFormat:getFormatter(longMonthYearFmt),longWeekdayFormat:getFormatter(longWeekdayFmt),narrowWeekdayFormat:getFormatter(narrowWeekdayFmt),yearFormat:getFormatter(yearFmt)};}

function getWeekdays(init){const{firstDayOfWeek=0,showWeekNumber=false,weekLabel,longWeekdayFormat,narrowWeekdayFormat}=init||{};const fixedFirstDayOfWeek=1+(firstDayOfWeek+(firstDayOfWeek<0?7:0))%7;const weekLabel2=weekLabel||'Wk';const initialValue=showWeekNumber?[{label:weekLabel2==='Wk'?'Week':weekLabel2,value:weekLabel2}]:[];const weekdays=Array.from(Array(7)).reduce((p,_,i)=>{const d=toUTCDate(2017,0,fixedFirstDayOfWeek+i);p.push({label:longWeekdayFormat(d),value:narrowWeekdayFormat(d)});return p;},initialValue);return weekdays;}

function getNormalizedDate(weekNumberType,date){const fy=date.getUTCFullYear();const m=date.getUTCMonth();const d=date.getUTCDate();const wd=date.getUTCDay();let offset=wd;if(weekNumberType==='first-4-day-week')offset=3;if(weekNumberType==='first-day-of-year')offset=6;if(weekNumberType==='first-full-week')offset=0;return toUTCDate(fy,m,d-wd+offset);}function getWeekNumber(weekNumberType,date){const normalizedDate=getNormalizedDate(weekNumberType,date);const firstDayOfYear=toUTCDate(normalizedDate.getUTCFullYear(),0,1);const numDays=1+(+normalizedDate-+firstDayOfYear)/864e5;return Math.ceil(numDays/7);}

function toValidWeekday(weekday){if(weekday>=0&&weekday<7)return Math.abs(weekday);const weekdayOffset=weekday<0?7*Math.ceil(Math.abs(weekday)):0;return (weekdayOffset+weekday)%7;}

function normalizeWeekday(weekDay,firstDayOfWeek,showWeekNumber){const x=toValidWeekday(weekDay-firstDayOfWeek);return showWeekNumber?1+x:x;}

function calendar(init){const{date,dayFormat,disabledDates=[],disabledDays=[],firstDayOfWeek=0,fullDateFormat,locale='en-US',max,min,showWeekNumber=false,weekLabel='Week',weekNumberType='first-4-day-week'}=init||{};const firstDayOfWeek2=toValidWeekday(firstDayOfWeek);const dateYear=date.getUTCFullYear();const dateMonth=date.getUTCMonth();const firstDateOfMonth=toUTCDate(dateYear,dateMonth,1);const disabledDaysSet=new Set(disabledDays.map(n=>normalizeWeekday(n,firstDayOfWeek2,showWeekNumber)));const disabledDatesSet=new Set(disabledDates.map(n=>+n));const calendarKey=[firstDateOfMonth.toJSON(),firstDayOfWeek2,locale,null==max?'':max.toJSON(),null==min?'':min.toJSON(),Array.from(disabledDaysSet).join(','),Array.from(disabledDatesSet).join(','),weekNumberType].filter(Boolean).join(':');const firstDayOfWeekOffset=normalizeWeekday(firstDateOfMonth.getUTCDay(),firstDayOfWeek2,showWeekNumber);const minTime=null==min?+new Date('2000-01-01'):+min;const maxTime=null==max?+new Date('2100-12-31'):+max;const colNum=showWeekNumber?8:7;const totalDays=toUTCDate(dateYear,1+dateMonth,0).getUTCDate();const rows=[];let cols=[];let calendarComplete=false;let curDay=1;for(const row of [0,1,2,3,4,5]){for(const col of [0,1,2,3,4,5,6].concat(colNum===7?[]:[7])){const idx=col+row*colNum;if(!calendarComplete&&showWeekNumber&&col===0){const weekNumberOffset=row<1?firstDayOfWeek2:0;const weekNumber=getWeekNumber(weekNumberType,toUTCDate(dateYear,dateMonth,curDay-weekNumberOffset));const wkLabel=`${weekLabel} ${weekNumber}`;cols.push({fullDate:null,label:wkLabel,value:`${weekNumber}`,key:`${calendarKey}:${wkLabel}`,disabled:true});continue;}if(calendarComplete||idx<firstDayOfWeekOffset){cols.push({fullDate:null,label:'',value:'',key:`${calendarKey}:${idx}`,disabled:true});continue;}const curDate=toUTCDate(dateYear,dateMonth,curDay);const curTime=+curDate;const isDisabledDay=disabledDaysSet.has(col)||disabledDatesSet.has(curTime)||curTime<minTime||curTime>maxTime;if(isDisabledDay)disabledDatesSet.add(curTime);cols.push({fullDate:curDate,label:fullDateFormat(curDate),value:dayFormat(curDate),key:`${calendarKey}:${curDate.toJSON()}`,disabled:isDisabledDay});curDay+=1;if(curDay>totalDays)calendarComplete=true;}rows.push(cols);cols=[];}return {disabledDatesSet,calendar:rows,disabledDaysSet:new Set(disabledDays.map(n=>toValidWeekday(n))),key:calendarKey};}

function getMultiCalendars(options){const{dayFormat,fullDateFormat,locale,longWeekdayFormat,narrowWeekdayFormat,selectedDate,disabledDates,disabledDays,firstDayOfWeek,max,min,showWeekNumber,weekLabel,weekNumberType}=options;const minTime=min==null?Number.MIN_SAFE_INTEGER:+min;const maxTime=max==null?Number.MAX_SAFE_INTEGER:+max;const weekdays=getWeekdays({longWeekdayFormat,narrowWeekdayFormat,firstDayOfWeek,showWeekNumber,weekLabel});const getKey=date=>[locale,date.toJSON(),disabledDates===null||disabledDates===void 0?void 0:disabledDates.join('_'),disabledDays===null||disabledDays===void 0?void 0:disabledDays.join('_'),firstDayOfWeek,max===null||max===void 0?void 0:max.toJSON(),min===null||min===void 0?void 0:min.toJSON(),showWeekNumber,weekLabel,weekNumberType].filter(Boolean).join(':');const ify=selectedDate.getUTCFullYear();const im=selectedDate.getUTCMonth();const calendarsList=[-1,0,1].map(n=>{const firstDayOfMonth=toUTCDate(ify,im+n,1);const lastDayOfMonthTime=+toUTCDate(ify,im+n+1,0);const key=getKey(firstDayOfMonth);if(lastDayOfMonthTime<minTime||+firstDayOfMonth>maxTime){return {key,calendar:[],disabledDatesSet:new Set(),disabledDaysSet:new Set()};}const calendarDays=calendar({dayFormat,fullDateFormat,locale,disabledDates,disabledDays,firstDayOfWeek,max,min,showWeekNumber,weekLabel,weekNumberType,date:firstDayOfMonth});return {...calendarDays,key};});const calendars=[];const $disabledDatesSet=new Set();const $disabledDaysSet=new Set();for(const cal of calendarsList){const{disabledDatesSet,disabledDaysSet,...rest}=cal;if(rest.calendar.length>0){if(disabledDaysSet.size>0){for(const o of disabledDaysSet)$disabledDaysSet.add(o);}if(disabledDatesSet.size>0){for(const o of disabledDatesSet)$disabledDatesSet.add(o);}}calendars.push(rest);}return {calendars,weekdays,disabledDatesSet:$disabledDatesSet,disabledDaysSet:$disabledDaysSet,key:getKey(selectedDate)};}

function getResolvedDate(date){const dateDate=date==null?new Date():new Date(date);const isUTCDateFormat=typeof date==='string'&&(/^\d{4}-\d{2}-\d{2}$/i.test(date)||/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}(Z|\+00:00|-00:00)$/i.test(date));const isUnixTimestamp=typeof date==='number'&&date>0&&isFinite(date);let fy=dateDate.getFullYear();let m=dateDate.getMonth();let d=dateDate.getDate();if(isUTCDateFormat||isUnixTimestamp){fy=dateDate.getUTCFullYear();m=dateDate.getUTCMonth();d=dateDate.getUTCDate();}return toUTCDate(fy,m,d);}

function getResolvedLocale(){return INTL_DATE_TIME_FORMAT&&INTL_DATE_TIME_FORMAT().resolvedOptions&&INTL_DATE_TIME_FORMAT().resolvedOptions().locale||'en-US';}

function hasClass(target,className){return target.classList.contains(className);}

function isValidDate(date,dateDate){return !(date==null||!(dateDate instanceof Date)||isNaN(+dateDate));}

function makeNumberPrecise(num){return num-Math.floor(num)>0?+num.toFixed(3):num;}

function passiveHandler(cb){return {passive:true,handleEvent:cb};}

function splitString(dateString,cb){const dateList=typeof dateString==='string'&&dateString.length>0?dateString.split(/,\s*/i):[];if(!dateList.length)return [];return typeof cb==='function'?dateList.map(cb):dateList;}

function targetScrollTo(target,scrollToOptions){if(target.scrollTo==null){const{top,left}=scrollToOptions||{};target.scrollTop=top||0;target.scrollLeft=left||0;}else {target.scrollTo(scrollToOptions);}}

function toFormattedDateString(date){if(date instanceof Date&&!isNaN(+date)){const dateString=date.toJSON();return dateString==null?'':dateString.replace(/^(.+)T.+/i,'$1');}return '';}

function toYearList(min,max){if(getDateRange(min,max)<864e5)return [];const fy=min.getUTCFullYear();return Array.from(Array(max.getUTCFullYear()-fy+1),(_,i)=>i+fy);}

function updateYearWithMinMax(date,min,max){const dateTime=typeof date==='number'?date:+date;const minTime=+min;const maxTime=+max;if(dateTime<minTime)return minTime;if(dateTime>maxTime)return maxTime;return date;}

function toPointer(ev){const{clientX,clientY,pageX,pageY}=ev;const x=Math.max(pageX,clientX);const y=Math.max(pageY,clientY);const id=ev.identifier||ev.pointerId;return {x,y,id:id==null?0:id};}function getFirstTouch(startPointer,ev){const changedTouches=ev.changedTouches;if(changedTouches==null)return {newPointer:toPointer(ev),oldPointer:startPointer};const touches=Array.from(changedTouches,n=>toPointer(n));const newPointer=startPointer==null?touches[0]:touches.find(n=>n.id===startPointer.id);return {newPointer,oldPointer:startPointer};}function addPassiveEventListener(node,event,callback){node.addEventListener(event,callback,supportsPassiveEventListener?{passive:true}:false);}class Tracker{constructor(_element,handlers){this._element=_element;this._startPointer=null;const{down,move,up}=handlers;this._down=this._onDown(down);this._move=this._onMove(move);this._up=this._onUp(up);if(_element&&_element.addEventListener){_element.addEventListener('mousedown',this._down);addPassiveEventListener(_element,'touchstart',this._down);addPassiveEventListener(_element,'touchmove',this._move);addPassiveEventListener(_element,'touchend',this._up);}}disconnect(){const rootEl=this._element;if(rootEl&&rootEl.removeEventListener){rootEl.removeEventListener('mousedown',this._down);rootEl.removeEventListener('touchstart',this._down);rootEl.removeEventListener('touchmove',this._move);rootEl.removeEventListener('touchend',this._up);}}_onDown(down){return ev=>{if(ev instanceof MouseEvent){this._element.addEventListener('mousemove',this._move);this._element.addEventListener('mouseup',this._up);this._element.addEventListener('mouseleave',this._up);}const{newPointer}=getFirstTouch(this._startPointer,ev);down(newPointer,ev);this._startPointer=newPointer;};}_onMove(move){return ev=>{this._updatePointers(move,ev);};}_onUp(up){return ev=>{this._updatePointers(up,ev,true);};}_updatePointers(cb,ev,shouldReset){if(shouldReset&&ev instanceof MouseEvent){this._element.removeEventListener('mousemove',this._move);this._element.removeEventListener('mouseup',this._up);this._element.removeEventListener('mouseleave',this._up);}const{newPointer,oldPointer}=getFirstTouch(this._startPointer,ev);cb(newPointer,oldPointer,ev);this._startPointer=shouldReset?null:newPointer;}}

class Datepicker extends s{constructor(){super();this.firstDayOfWeek=0;this.showWeekNumber=false;this.weekNumberType='first-4-day-week';this.landscape=false;this.locale=getResolvedLocale();this.disabledDays='';this.disabledDates='';this.weekLabel='Wk';this.inline=false;this.dragRatio=.15;this._hasMin=false;this._hasMax=false;this._disabledDaysSet=new Set();this._disabledDatesSet=new Set();this._dx=-Infinity;this._hasNativeWebAnimation='animate'in HTMLElement.prototype;this._updatingDateWithKey=false;const todayDate=getResolvedDate();const allFormatters=getFormatters(this.locale);const formattedTodayDate=toFormattedDateString(todayDate);const max=getResolvedDate('2100-12-31');this.value=formattedTodayDate;this.startView='calendar';this._min=new Date(todayDate);this._max=new Date(max);this._todayDate=todayDate;this._maxDate=max;this._yearList=toYearList(todayDate,max);this._selectedDate=new Date(todayDate);this._focusedDate=new Date(todayDate);this._formatters=allFormatters;}get startView(){return this._startView;}set startView(val){const defaultVal=!val?'calendar':val;if(defaultVal!=='calendar'&&defaultVal!=='yearList')return;const oldVal=this._startView;this._startView=defaultVal;this.requestUpdate('startView',oldVal);}get min(){return this._hasMin?toFormattedDateString(this._min):'';}set min(val){const valDate=getResolvedDate(val);const isValidMin=isValidDate(val,valDate);this._min=isValidMin?valDate:this._todayDate;this._hasMin=isValidMin;this.requestUpdate('min');}get max(){return this._hasMax?toFormattedDateString(this._max):'';}set max(val){const valDate=getResolvedDate(val);const isValidMax=isValidDate(val,valDate);this._max=isValidMax?valDate:this._maxDate;this._hasMax=isValidMax;this.requestUpdate('max');}get value(){return toFormattedDateString(this._focusedDate);}set value(val){const valDate=getResolvedDate(val);const validValue=isValidDate(val,valDate)?valDate:this._todayDate;this._focusedDate=new Date(validValue);this._selectedDate=this._lastSelectedDate=new Date(validValue);}disconnectedCallback(){super.disconnectedCallback();if(this._tracker){this._tracker.disconnect();this._tracker=undefined;}}render(){if(this._formatters.locale!==this.locale)this._formatters=getFormatters(this.locale);const datepickerBodyContent='yearList'===this._startView?this._renderDatepickerYearList():this._renderDatepickerCalendar();const datepickerHeaderContent=this.inline?null:$`<div class="datepicker-header" part="header">${this._renderHeaderSelectorButton()}</div>`;return $`
    ${datepickerHeaderContent}
    <div class="datepicker-body" part="body">${d(datepickerBodyContent)}</div>
    `;}firstUpdated(){let firstFocusableElement;if('calendar'===this._startView){firstFocusableElement=this.inline?this.shadowRoot.querySelector('.btn__month-selector'):this._buttonSelectorYear;}else {firstFocusableElement=this._yearViewListItem;}dispatchCustomEvent(this,'datepicker-first-updated',{firstFocusableElement,value:this.value});}async updated(changed){const startView=this._startView;if(changed.has('min')||changed.has('max')){this._yearList=toYearList(this._min,this._max);if('yearList'===startView)this.requestUpdate();const minTime=+this._min;const maxTime=+this._max;if(getDateRange(minTime,maxTime)>864e5){const focusedDateTime=+this._focusedDate;let newValue=focusedDateTime;if(focusedDateTime<minTime)newValue=minTime;if(focusedDateTime>maxTime)newValue=maxTime;this.value=toFormattedDateString(new Date(newValue));}}if(changed.has('_startView')||changed.has('startView')){if('yearList'===startView){const selectedYearScrollTop=48*(this._selectedDate.getUTCFullYear()-this._min.getUTCFullYear()-2);targetScrollTo(this._yearViewFullList,{top:selectedYearScrollTop,left:0});}if('calendar'===startView&&null==this._tracker){const calendarsContainer=this.calendarsContainer;let $down=false;let $move=false;let $transitioning=false;if(calendarsContainer){const handlers={down:()=>{if($transitioning)return;$down=true;this._dx=0;},move:(pointer,oldPointer)=>{if($transitioning||!$down)return;const dx=this._dx;const hasMin=dx<0&&hasClass(calendarsContainer,'has-max-date')||dx>0&&hasClass(calendarsContainer,'has-min-date');if(!hasMin&&Math.abs(dx)>0&&$down){$move=true;calendarsContainer.style.transform=`translateX(${makeNumberPrecise(dx)}px)`;}this._dx=hasMin?0:dx+(pointer.x-oldPointer.x);},up:async(_$,_$$,ev)=>{if($down&&$move){const dx=this._dx;const maxWidth=calendarsContainer.getBoundingClientRect().width/3;const didPassThreshold=Math.abs(dx)>Number(this.dragRatio)*maxWidth;const transitionDuration=350;const transitionEasing='cubic-bezier(0, 0, .4, 1)';const transformTo=didPassThreshold?makeNumberPrecise(maxWidth*(dx<0?-1:1)):0;$transitioning=true;await animateElement(calendarsContainer,{hasNativeWebAnimation:this._hasNativeWebAnimation,keyframes:[{transform:`translateX(${dx}px)`},{transform:`translateX(${transformTo}px)`}],options:{duration:transitionDuration,easing:transitionEasing}});if(didPassThreshold){this._updateMonth(dx<0?'next':'previous').handleEvent();}$down=$move=$transitioning=false;this._dx=-Infinity;calendarsContainer.removeAttribute('style');dispatchCustomEvent(this,'datepicker-animation-finished');}else if($down){this._updateFocusedDate(ev);$down=$move=false;this._dx=-Infinity;}}};this._tracker=new Tracker(calendarsContainer,handlers);}}if(changed.get('_startView')&&'calendar'===startView){this._focusElement('[part="year-selector"]');}}if(this._updatingDateWithKey){this._focusElement('[part="calendars"]:nth-of-type(2) .day--focused');this._updatingDateWithKey=false;}}_focusElement(selector){const focusedTarget=this.shadowRoot.querySelector(selector);if(focusedTarget)focusedTarget.focus();}_renderHeaderSelectorButton(){const{yearFormat,dateFormat}=this._formatters;const isCalendarView=this.startView==='calendar';const focusedDate=this._focusedDate;const formattedDate=dateFormat(focusedDate);const formatterFy=yearFormat(focusedDate);return $`
    <button
      class="${o({'btn__year-selector':true,selected:!isCalendarView})}"
      type="button"
      part="year-selector"
      data-view="${'yearList'}"
      @click="${this._updateView('yearList')}">${formatterFy}</button>

    <div class="datepicker-toolbar" part="toolbar">
      <button
        class="${o({'btn__calendar-selector':true,selected:isCalendarView})}"
        type="button"
        part="calendar-selector"
        data-view="${'calendar'}"
        @click="${this._updateView('calendar')}">${formattedDate}</button>
    </div>
    `;}_renderDatepickerYearList(){const{yearFormat}=this._formatters;const focusedDateFy=this._focusedDate.getUTCFullYear();return $`
    <div class="datepicker-body__year-list-view" part="year-list-view">
      <div class="year-list-view__full-list" part="year-list" @click="${this._updateYear}">
      ${this._yearList.map(n=>$`<button
        class="${o({'year-list-view__list-item':true,'year--selected':focusedDateFy===n})}"
        type="button"
        part="year"
        .year="${n}">${yearFormat(toUTCDate(n,0,1))}</button>`)}</div>
    </div>
    `;}_renderDatepickerCalendar(){const{longMonthYearFormat,dayFormat,fullDateFormat,longWeekdayFormat,narrowWeekdayFormat}=this._formatters;const disabledDays=splitString(this.disabledDays,Number);const disabledDates=splitString(this.disabledDates,getResolvedDate);const showWeekNumber=this.showWeekNumber;const $focusedDate=this._focusedDate;const firstDayOfWeek=this.firstDayOfWeek;const todayDate=getResolvedDate();const $selectedDate=this._selectedDate;const $max=this._max;const $min=this._min;const{calendars,disabledDaysSet,disabledDatesSet,weekdays}=getMultiCalendars({dayFormat,fullDateFormat,longWeekdayFormat,narrowWeekdayFormat,firstDayOfWeek,disabledDays,disabledDates,locale:this.locale,selectedDate:$selectedDate,showWeekNumber:this.showWeekNumber,weekNumberType:this.weekNumberType,max:$max,min:$min,weekLabel:this.weekLabel});const hasMinDate=!calendars[0].calendar.length;const hasMaxDate=!calendars[2].calendar.length;const weekdaysContent=weekdays.map(o=>$`<th
        class="calendar-weekday"
        part="calendar-weekday"
        role="columnheader"
        aria-label="${o.label}"
      >
        <div class="weekday" part="weekday">${o.value}</div>
      </th>`);const calendarsContent=c(calendars,n=>n.key,({calendar},ci)=>{if(!calendar.length){return $`<div class="calendar-container" part="calendar"></div>`;}const calendarAriaId=`calendarcaption${ci}`;const midCalendarFullDate=calendar[1][1].fullDate;const isMidCalendar=ci===1;const $newFocusedDate=isMidCalendar&&!this._isInVisibleMonth($focusedDate,$selectedDate)?computeNextFocusedDate({disabledDaysSet,disabledDatesSet,hasAltKey:false,keyCode:36,focusedDate:$focusedDate,selectedDate:$selectedDate,minTime:+$min,maxTime:+$max}):$focusedDate;return $`
      <div class="calendar-container" part="calendar">
        <table class="calendar-table" part="table" role="grid" aria-labelledby="${calendarAriaId}">
          <caption id="${calendarAriaId}">
            <div class="calendar-label" part="label">${midCalendarFullDate?longMonthYearFormat(midCalendarFullDate):''}</div>
          </caption>

          <thead role="rowgroup">
            <tr class="calendar-weekdays" part="weekdays" role="row">${weekdaysContent}</tr>
          </thead>

          <tbody role="rowgroup">${calendar.map(calendarRow=>{return $`<tr role="row">${calendarRow.map((calendarCol,i)=>{const{disabled,fullDate,label,value}=calendarCol;if(!fullDate&&value&&showWeekNumber&&i<1){return $`<th
                      class="full-calendar__day weekday-label"
                      part="calendar-day"
                      scope="row"
                      role="rowheader"
                      abbr="${label}"
                      aria-label="${label}"
                    >${value}</th>`;}if(!value||!fullDate){return $`<td class="full-calendar__day day--empty" part="calendar-day"></td>`;}const curTime=+new Date(fullDate);const isCurrentDate=+$focusedDate===curTime;const shouldTab=isMidCalendar&&$newFocusedDate.getUTCDate()===Number(value);return $`
                  <td
                    tabindex="${shouldTab?'0':'-1'}"
                    class="${o({'full-calendar__day':true,'day--disabled':disabled,'day--today':+todayDate===curTime,'day--focused':!disabled&&isCurrentDate})}"
                    part="calendar-day"
                    role="gridcell"
                    aria-disabled="${disabled?'true':'false'}"
                    aria-label="${label}"
                    aria-selected="${isCurrentDate?'true':'false'}"
                    .fullDate="${fullDate}"
                    .day="${value}"
                  >
                    <div class="calendar-day" part="day">${value}</div>
                  </td>
                  `;})}</tr>`;})}</tbody>
        </table>
      </div>
      `;});this._disabledDatesSet=disabledDatesSet;this._disabledDaysSet=disabledDaysSet;return $`
    <div class="datepicker-body__calendar-view" part="calendar-view">
      <div class="calendar-view__month-selector" part="month-selectors">
        <div class="month-selector-container">${hasMinDate?null:$`
          <button
            class="btn__month-selector"
            type="button"
            part="month-selector"
            aria-label="Previous month"
            @click="${this._updateMonth('previous')}"
          >${iconChevronLeft}</button>
        `}</div>

        <div class="month-selector-container">${hasMaxDate?null:$`
          <button
            class="btn__month-selector"
            type="button"
            part="month-selector"
            aria-label="Next month"
            @click="${this._updateMonth('next')}"
          >${iconChevronRight}</button>
        `}</div>
      </div>

      <div
        class="${o({'calendars-container':true,'has-min-date':hasMinDate,'has-max-date':hasMaxDate})}"
        part="calendars"
        @keyup="${this._updateFocusedDateWithKeyboard}"
      >${calendarsContent}</div>
    </div>
    `;}_updateView(view){const handleUpdateView=()=>{if('calendar'===view){this._selectedDate=this._lastSelectedDate=new Date(updateYearWithMinMax(this._focusedDate,this._min,this._max));}this._startView=view;};return passiveHandler(handleUpdateView);}_updateMonth(updateType){const handleUpdateMonth=()=>{const calendarsContainer=this.calendarsContainer;if(null==calendarsContainer)return this.updateComplete;const dateDate=this._lastSelectedDate||this._selectedDate;const minDate=this._min;const maxDate=this._max;const isPreviousMonth=updateType==='previous';const newSelectedDate=toUTCDate(dateDate.getUTCFullYear(),dateDate.getUTCMonth()+(isPreviousMonth?-1:1),1);const newSelectedDateFy=newSelectedDate.getUTCFullYear();const newSelectedDateM=newSelectedDate.getUTCMonth();const minDateFy=minDate.getUTCFullYear();const minDateM=minDate.getUTCMonth();const maxDateFy=maxDate.getUTCFullYear();const maxDateM=maxDate.getUTCMonth();const isLessThanYearAndMonth=newSelectedDateFy<minDateFy||newSelectedDateFy<=minDateFy&&newSelectedDateM<minDateM;const isMoreThanYearAndMonth=newSelectedDateFy>maxDateFy||newSelectedDateFy>=maxDateFy&&newSelectedDateM>maxDateM;if(isLessThanYearAndMonth||isMoreThanYearAndMonth)return this.updateComplete;this._lastSelectedDate=newSelectedDate;this._selectedDate=this._lastSelectedDate;return this.updateComplete;};return passiveHandler(handleUpdateMonth);}_updateYear(ev){const selectedYearEl=findShadowTarget(ev,n=>hasClass(n,'year-list-view__list-item'));if(selectedYearEl==null)return;const newFocusedDate=updateYearWithMinMax(new Date(this._focusedDate).setUTCFullYear(+selectedYearEl.year),this._min,this._max);this._selectedDate=this._lastSelectedDate=new Date(newFocusedDate);this._focusedDate=new Date(newFocusedDate);this._startView='calendar';}_updateFocusedDate(ev){const selectedDayEl=findShadowTarget(ev,n=>hasClass(n,'full-calendar__day'));if(selectedDayEl==null||['day--empty','day--disabled','day--focused','weekday-label'].some(n=>hasClass(selectedDayEl,n)))return;this._focusedDate=new Date(selectedDayEl.fullDate);dispatchCustomEvent(this,'datepicker-value-updated',{isKeypress:false,value:this.value});}_updateFocusedDateWithKeyboard(ev){const keyCode=ev.keyCode;if(13===keyCode||32===keyCode){dispatchCustomEvent(this,'datepicker-value-updated',{keyCode,isKeypress:true,value:this.value});this._focusedDate=new Date(this._selectedDate);return;}if(keyCode===9||!ALL_NAV_KEYS_SET.has(keyCode))return;const selectedDate=this._selectedDate;const nextFocusedDate=computeNextFocusedDate({keyCode,selectedDate,disabledDatesSet:this._disabledDatesSet,disabledDaysSet:this._disabledDaysSet,focusedDate:this._focusedDate,hasAltKey:ev.altKey,maxTime:+this._max,minTime:+this._min});if(!this._isInVisibleMonth(nextFocusedDate,selectedDate)){this._selectedDate=this._lastSelectedDate=nextFocusedDate;}this._focusedDate=nextFocusedDate;this._updatingDateWithKey=true;dispatchCustomEvent(this,'datepicker-value-updated',{keyCode,isKeypress:true,value:this.value});}_isInVisibleMonth(dateA,dateB){const dateAFy=dateA.getUTCFullYear();const dateAM=dateA.getUTCMonth();const dateBFY=dateB.getUTCFullYear();const dateBM=dateB.getUTCMonth();return dateAFy===dateBFY&&dateAM===dateBM;}get calendarsContainer(){return this.shadowRoot.querySelector('.calendars-container');}}Datepicker.styles=[datepickerVariables,resetButton,r`
    :host {
      width: 312px;
      /** NOTE: Magic number as 16:9 aspect ratio does not look good */
      /* height: calc((var(--app-datepicker-width) / .66) - var(--app-datepicker-footer-height, 56px)); */
      background-color: var(--app-datepicker-bg-color, #fff);
      color: var(--app-datepicker-color, #000);
      border-radius:
        var(--app-datepicker-border-top-left-radius, 0)
        var(--app-datepicker-border-top-right-radius, 0)
        var(--app-datepicker-border-bottom-right-radius, 0)
        var(--app-datepicker-border-bottom-left-radius, 0);
      contain: content;
      overflow: hidden;
    }
    :host([landscape]) {
      display: flex;

      /** <iphone-5-landscape-width> - <standard-side-margin-width> */
      min-width: calc(568px - 16px * 2);
      width: calc(568px - 16px * 2);
    }

    .datepicker-header + .datepicker-body {
      border-top: 1px solid var(--app-datepicker-separator-color, #ddd);
    }
    :host([landscape]) > .datepicker-header + .datepicker-body {
      border-top: none;
      border-left: 1px solid var(--app-datepicker-separator-color, #ddd);
    }

    .datepicker-header {
      display: flex;
      flex-direction: column;
      align-items: flex-start;

      position: relative;
      padding: 16px 24px;
    }
    :host([landscape]) > .datepicker-header {
      /** :this.<one-liner-month-day-width> + :this.<side-padding-width> */
      min-width: calc(14ch + 24px * 2);
    }

    .btn__year-selector,
    .btn__calendar-selector {
      color: var(--app-datepicker-selector-color, rgba(0, 0, 0, .55));
      cursor: pointer;
      /* outline: none; */
    }
    .btn__year-selector.selected,
    .btn__calendar-selector.selected {
      color: currentColor;
    }

    /**
      * NOTE: IE11-only fix. This prevents formatted focused date from overflowing the container.
      */
    .datepicker-toolbar {
      width: 100%;
    }

    .btn__year-selector {
      font-size: 16px;
      font-weight: 700;
    }
    .btn__calendar-selector {
      font-size: 36px;
      font-weight: 700;
      line-height: 1;
    }

    .datepicker-body {
      position: relative;
      width: 100%;
      overflow: hidden;
    }

    .datepicker-body__calendar-view {
      min-height: 56px;
    }

    .calendar-view__month-selector {
      display: flex;
      align-items: center;

      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      padding: 0 8px;
      z-index: 1;
    }

    .month-selector-container {
      max-height: 56px;
      height: 100%;
    }
    .month-selector-container + .month-selector-container {
      margin: 0 0 0 auto;
    }

    .btn__month-selector {
      padding: calc((56px - 24px) / 2);
      /**
        * NOTE: button element contains no text, only SVG.
        * No extra height will incur with such setting.
        */
      line-height: 0;
    }
    .btn__month-selector > svg {
      fill: currentColor;
    }

    .calendars-container {
      display: flex;
      justify-content: center;

      position: relative;
      top: 0;
      left: calc(-100%);
      width: calc(100% * 3);
      transform: translateZ(0);
      will-change: transform;
      /**
        * NOTE: Required for Pointer Events API to work on touch devices.
        * Native \`pan-y\` action will be fired by the browsers since we only care about the
        * horizontal direction. This is great as vertical scrolling still works even when touch
        * event happens on a datepicker's calendar.
        */
      touch-action: pan-y;
      /* outline: none; */
    }

    .year-list-view__full-list {
      max-height: calc(48px * 7);
      overflow-y: auto;

      scrollbar-color: var(--app-datepicker-scrollbar-thumb-bg-color, rgba(0, 0, 0, .35)) rgba(0, 0, 0, 0);
      scrollbar-width: thin;
    }
    .year-list-view__full-list::-webkit-scrollbar {
      width: 8px;
      background-color: rgba(0, 0, 0, 0);
    }
    .year-list-view__full-list::-webkit-scrollbar-thumb {
      background-color: var(--app-datepicker-scrollbar-thumb-bg-color, rgba(0, 0, 0, .35));
      border-radius: 50px;
    }
    .year-list-view__full-list::-webkit-scrollbar-thumb:hover {
      background-color: var(--app-datepicker-scrollbar-thumb-hover-bg-color, rgba(0, 0, 0, .5));
    }

    .calendar-weekdays > th,
    .weekday-label {
      color: var(--app-datepicker-weekday-color, rgba(0, 0, 0, .55));
      font-weight: 400;
      transform: translateZ(0);
      will-change: transform;
    }

    .calendar-container,
    .calendar-label,
    .calendar-table {
      width: 100%;
    }

    .calendar-container {
      position: relative;
      padding: 0 16px 16px;
    }

    .calendar-table {
      -moz-user-select: none;
      -webkit-user-select: none;
      user-select: none;

      border-collapse: collapse;
      border-spacing: 0;
      text-align: center;
    }

    .calendar-label {
      display: flex;
      align-items: center;
      justify-content: center;

      height: 56px;
      font-weight: 500;
      text-align: center;
    }

    .calendar-weekday,
    .full-calendar__day {
      position: relative;
      width: calc(100% / 7);
      height: 0;
      padding: calc(100% / 7 / 2) 0;
      outline: none;
      text-align: center;
    }
    .full-calendar__day:not(.day--disabled):focus {
      outline: #000 dotted 1px;
      outline: -webkit-focus-ring-color auto 1px;
    }
    :host([showweeknumber]) .calendar-weekday,
    :host([showweeknumber]) .full-calendar__day {
      width: calc(100% / 8);
      padding-top: calc(100% / 8);
      padding-bottom: 0;
    }
    :host([showweeknumber]) th.weekday-label {
      padding: 0;
    }

    /**
      * NOTE: Interesting fact! That is ::after will trigger paint when dragging. This will trigger
      * layout and paint on **ONLY** affected nodes. This is much cheaper as compared to rendering
      * all :::after of all calendar day elements. When dragging the entire calendar container,
      * because of all layout and paint trigger on each and every ::after, this becomes a expensive
      * task for the browsers especially on low-end devices. Even though animating opacity is much
      * cheaper, the technique does not work here. Adding 'will-change' will further reduce overall
      * painting at the expense of memory consumption as many cells in a table has been promoted
      * a its own layer.
      */
    .full-calendar__day:not(.day--empty):not(.day--disabled):not(.weekday-label) {
      transform: translateZ(0);
      will-change: transform;
    }
    .full-calendar__day:not(.day--empty):not(.day--disabled):not(.weekday-label).day--focused::after,
    .full-calendar__day:not(.day--empty):not(.day--disabled):not(.day--focused):not(.weekday-label):hover::after {
      content: '';
      display: block;
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: var(--app-datepicker-accent-color, #1a73e8);
      border-radius: 50%;
      opacity: 0;
      pointer-events: none;
    }
    .full-calendar__day:not(.day--empty):not(.day--disabled):not(.weekday-label) {
      cursor: pointer;
      pointer-events: auto;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    }
    .full-calendar__day.day--focused:not(.day--empty):not(.day--disabled):not(.weekday-label)::after,
    .full-calendar__day.day--today.day--focused:not(.day--empty):not(.day--disabled):not(.weekday-label)::after {
      opacity: 1;
    }

    .calendar-weekday > .weekday,
    .full-calendar__day > .calendar-day {
      display: flex;
      align-items: center;
      justify-content: center;

      position: absolute;
      top: 5%;
      left: 5%;
      width: 90%;
      height: 90%;
      color: currentColor;
      font-size: 14px;
      pointer-events: none;
      z-index: 1;
    }
    .full-calendar__day.day--today {
      color: var(--app-datepicker-accent-color, #1a73e8);
    }
    .full-calendar__day.day--focused,
    .full-calendar__day.day--today.day--focused {
      color: var(--app-datepicker-focused-day-color, #fff);
    }
    .full-calendar__day.day--empty,
    .full-calendar__day.weekday-label,
    .full-calendar__day.day--disabled > .calendar-day {
      pointer-events: none;
    }
    .full-calendar__day.day--disabled:not(.day--today) {
      color: var(--app-datepicker-disabled-day-color, rgba(0, 0, 0, .55));
    }

    .year-list-view__list-item {
      position: relative;
      width: 100%;
      padding: 12px 16px;
      text-align: center;
      /** NOTE: Reduce paint when hovering and scrolling, but this increases memory usage */
      /* will-change: opacity; */
      /* outline: none; */
    }
    .year-list-view__list-item::after {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: var(--app-datepicker-focused-year-bg-color, #000);
      opacity: 0;
      pointer-events: none;
    }
    .year-list-view__list-item:focus::after {
      opacity: .05;
    }
    .year-list-view__list-item.year--selected {
      color: var(--app-datepicker-accent-color, #1a73e8);
      font-size: 24px;
      font-weight: 500;
    }

    @media (any-hover: hover) {
      .btn__month-selector:hover,
      .year-list-view__list-item:hover {
        cursor: pointer;
      }
      .full-calendar__day:not(.day--empty):not(.day--disabled):not(.day--focused):not(.weekday-label):hover::after {
        opacity: .15;
      }
      .year-list-view__list-item:hover::after {
        opacity: .05;
      }
    }

    @supports (background: -webkit-canvas(squares)) {
      .calendar-container {
        padding: 56px 16px 16px;
      }

      table > caption {
        position: absolute;
        top: 0;
        left: 50%;
        transform: translate3d(-50%, 0, 0);
        will-change: transform;
      }
    }
    `];__decorate([e({type:Number,reflect:true})],Datepicker.prototype,"firstDayOfWeek",void 0);__decorate([e({type:Boolean,reflect:true})],Datepicker.prototype,"showWeekNumber",void 0);__decorate([e({type:String,reflect:true})],Datepicker.prototype,"weekNumberType",void 0);__decorate([e({type:Boolean,reflect:true})],Datepicker.prototype,"landscape",void 0);__decorate([e({type:String,reflect:true})],Datepicker.prototype,"startView",null);__decorate([e({type:String,reflect:true})],Datepicker.prototype,"min",null);__decorate([e({type:String,reflect:true})],Datepicker.prototype,"max",null);__decorate([e({type:String})],Datepicker.prototype,"value",null);__decorate([e({type:String})],Datepicker.prototype,"locale",void 0);__decorate([e({type:String})],Datepicker.prototype,"disabledDays",void 0);__decorate([e({type:String})],Datepicker.prototype,"disabledDates",void 0);__decorate([e({type:String})],Datepicker.prototype,"weekLabel",void 0);__decorate([e({type:Boolean})],Datepicker.prototype,"inline",void 0);__decorate([e({type:Number})],Datepicker.prototype,"dragRatio",void 0);__decorate([e({type:Date,attribute:false})],Datepicker.prototype,"_selectedDate",void 0);__decorate([e({type:Date,attribute:false})],Datepicker.prototype,"_focusedDate",void 0);__decorate([e({type:String,attribute:false})],Datepicker.prototype,"_startView",void 0);__decorate([i('.year-list-view__full-list')],Datepicker.prototype,"_yearViewFullList",void 0);__decorate([i('.btn__year-selector')],Datepicker.prototype,"_buttonSelectorYear",void 0);__decorate([i('.year-list-view__list-item')],Datepicker.prototype,"_yearViewListItem",void 0);__decorate([e$1({passive:true})],Datepicker.prototype,"_updateYear",null);__decorate([e$1({passive:true})],Datepicker.prototype,"_updateFocusedDateWithKeyboard",null);

function customElementsDefine(tagName,baseClass){if(window.customElements&&!window.customElements.get(tagName)){window.customElements.define(tagName,baseClass);}}

customElementsDefine(DATEPICKER_NAME,Datepicker);

let HaDialogDatePicker=_decorate([n("ha-dialog-date-picker")],function(_initialize,_LitElement){class HaDialogDatePicker extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HaDialogDatePicker,d:[{kind:"field",decorators:[e()],key:"value",value:void 0},{kind:"field",decorators:[e({type:Boolean})],key:"disabled",value(){return false;}},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[t()],key:"_params",value:void 0},{kind:"field",decorators:[t()],key:"_value",value:void 0},{kind:"method",key:"showDialog",value:function showDialog(params){this._params=params;this._value=params.value;}},{kind:"method",key:"closeDialog",value:function closeDialog(){this._params=undefined;fireEvent(this,"dialog-closed",{dialog:this.localName});}},{kind:"method",key:"render",value:function render(){if(!this._params){return $``;}return $`<ha-dialog open @closed=${this.closeDialog}>
      <app-datepicker
        .value=${this._value}
        .min=${this._params.min}
        .max=${this._params.max}
        .locale=${this._params.locale}
        @datepicker-value-updated=${this._valueChanged}
      ></app-datepicker>
      <mwc-button slot="secondaryAction" @click=${this._setToday}
        >today</mwc-button
      >
      <mwc-button slot="primaryAction" dialogaction="cancel" class="cancel-btn">
        cancel
      </mwc-button>
      <mwc-button slot="primaryAction" @click=${this._setValue}>ok</mwc-button>
    </ha-dialog>`;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){this._value=ev.detail.value;}},{kind:"method",key:"_setToday",value:function _setToday(){this._value=new Date().toISOString().split("T")[0];}},{kind:"method",key:"_setValue",value:function _setValue(){var _this$_params;(_this$_params=this._params)===null||_this$_params===void 0?void 0:_this$_params.onChange(this._value);this.closeDialog();}},{kind:"field",static:true,key:"styles",value(){return [haStyleDialog,r`
      ha-dialog {
        --dialog-content-padding: 0;
        --justify-action-buttons: space-between;
      }
      app-datepicker {
        --app-datepicker-accent-color: var(--primary-color);
        --app-datepicker-bg-color: transparent;
        --app-datepicker-color: var(--primary-text-color);
        --app-datepicker-disabled-day-color: var(--disabled-text-color);
        --app-datepicker-focused-day-color: var(--text-primary-color);
        --app-datepicker-focused-year-bg-color: var(--primary-color);
        --app-datepicker-selector-color: var(--secondary-text-color);
        --app-datepicker-separator-color: var(--divider-color);
        --app-datepicker-weekday-color: var(--secondary-text-color);
      }
      app-datepicker::part(calendar-day):focus {
        outline: none;
      }
      @media all and (min-width: 450px) {
        ha-dialog {
          --mdc-dialog-min-width: 300px;
        }
      }
      @media all and (max-width: 450px), all and (max-height: 500px) {
        app-datepicker {
          width: 100%;
        }
      }
    `];}}]};},s);

export { HaDialogDatePicker };
