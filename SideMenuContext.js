// SideMenuContext.js (Create a new context for the side menu state)
import React, { createContext, useContext, useState } from 'react';

const SideMenuContext = createContext();

export function useSideMenu() {
  return useContext(SideMenuContext);
}

export function SideMenuProvider({ children }) {
  const [isMenuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!isMenuOpen);
  };

  return (
    <SideMenuContext.Provider value={{ isMenuOpen, toggleMenu }}>
      {children}
    </SideMenuContext.Provider>
  );
}
