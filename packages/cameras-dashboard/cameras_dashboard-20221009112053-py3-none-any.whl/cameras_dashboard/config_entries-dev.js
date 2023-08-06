const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

const getConfigEntries=hass=>hass.callApi("GET","config/config_entries/entry");

export { getConfigEntries as g };
