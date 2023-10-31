import React, { createContext, useContext, useState } from 'react';

const ActiveTabContext = createContext();

export const useActiveTab = () => useContext(ActiveTabContext);

export const ActiveTabProvider = ({ children }) => {
  const [activeTab, setActiveTab] = useState('');

  const setTab = (tab) => {
    setActiveTab(tab);
  };

  return (
    <ActiveTabContext.Provider value={{ activeTab, setTab }}>
      {children}
    </ActiveTabContext.Provider>
  );
};