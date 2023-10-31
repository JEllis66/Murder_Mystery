import React, { createContext, useContext, useState } from 'react';

const ConfirmationContext = createContext();

export const useConfirmation = () => {
  return useContext(ConfirmationContext);
};

export const ConfirmationProvider = ({ children }) => {
  const [confirmationVisible, setConfirmationVisible] = useState(false);
  const [confirmationMessage, setConfirmationMessage] = useState('');
  const [onConfirmCallback, setOnConfirmCallback] = useState(null);
  const [command, setCommand] = useState('');

  const showConfirmation = (message, onConfirm, actionCommand) => {
    setConfirmationMessage(message);
    setOnConfirmCallback(() => onConfirm);
    setCommand(actionCommand);
    setConfirmationVisible(true);
  };

  const hideConfirmation = () => {
    setConfirmationVisible(false);
    setOnConfirmCallback(null);
  };

  return (
    <ConfirmationContext.Provider
      value={{
        confirmationVisible,
        confirmationMessage,
        showConfirmation,
        hideConfirmation,
        command,
        setCommand,
      }}
    >
      {children}
    </ConfirmationContext.Provider>
  );
};
