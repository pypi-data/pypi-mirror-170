const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

const FORMAT_NUMBER="number";const callAlarmAction=(hass,entity,action,code)=>{hass.callService("alarm_control_panel",`alarm_${action}`,{entity_id:entity,code});};

export { FORMAT_NUMBER as F, callAlarmAction as c };
