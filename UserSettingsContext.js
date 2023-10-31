import React, { createContext, useContext, useState } from 'react';

const UserSettingsContext = createContext();

export const useUserSettings = () => {
  return useContext(UserSettingsContext);
};

export const UserSettingsProvider = ({ children }) => {
  const [userSettings, setUserSettings] = useState({
    username: 'JEllis',
    user_privilege_level: 'Admin',
    app_title: "Lancaster's",
    default_app_color: '#6B001E',
    default_app_background_color: '#fff',
    font_color: '#DC4C64',
    primary_button_color: '#DC4C64',
  });

  const updateUserSettings = (newSettings) => {
    setUserSettings((prevSettings) => ({
      ...prevSettings,
      ...newSettings,
    }));
  };

  return (
    <UserSettingsContext.Provider value={{ userSettings, updateUserSettings }}>
      {children}
    </UserSettingsContext.Provider>
  );
};
