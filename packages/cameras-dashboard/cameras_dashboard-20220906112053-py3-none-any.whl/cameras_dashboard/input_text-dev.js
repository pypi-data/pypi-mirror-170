const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

const setValue=(hass,entity,value)=>hass.callService(entity.split(".",1)[0],"set_value",{value,entity_id:entity});

export { setValue as s };
