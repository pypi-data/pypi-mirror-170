const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

const triggerAutomationActions=(hass,entityId)=>{hass.callService("automation","trigger",{entity_id:entityId,skip_condition:true});};const subscribeTrigger=(hass,onChange,trigger,variables)=>hass.connection.subscribeMessage(onChange,{type:"subscribe_trigger",trigger,variables});

export { subscribeTrigger as s, triggerAutomationActions as t };
