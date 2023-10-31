import React, { useState } from 'react';
import Login from './Views/LoginPage.jsx';
import LoginLogo from './Views/LoginLogoPage.jsx';
import Home from './Views/HomePage.jsx'
import CreateApp from './Views/CreateAppPage.jsx';
import CreateCharacter from './Views/CreateCharacterPage.jsx';
import Dashboard from './Views/DashboardPage.jsx';
import AdminDashboard from './Views/AdminDashboardPage.jsx';
import AdminControls from './Views/AdminControlsPage.jsx'
import RequestPortal from './Views/RequestPortalPage.jsx';
import EventPortal from './Views/EventPortalPage.jsx'
import StoryItem from './Views/StoryItemPage.jsx';
import StoryItemEdit from './Views/StoryItemEditPage.jsx';
import CreateStoryItem from './Views/CreateStoryItemPage.jsx';
import CharacterPortal from './Views/CharacterPortalPage.jsx';
import CharacterEdit from './Views/CharacterEditPage.jsx'
import Journal from './Views/JournalPage.jsx';
import JournalLive from './Views/JournalLivePage.jsx';
import JournalEntries from './Views/JournalEntriesPage.jsx';
import JournalEntryNew from './Views/JournalEntryNewPage.jsx';
import JournalEdit from './Views/JournalEditPage.jsx';
import Database from './Views/DatabasePage.jsx';
import MyItems from './Views/MyItemsPage.jsx';
import StoryItemView from './Views/StoryItemViewPage.jsx';
import StoryItemJournalView from './Views/StoryItemJournalViewPage.jsx';
import StoryItemSearchView from './Views/StoryItemSearchViewPage.jsx';
import SearchDB from './Views/SearchDBPage.jsx';
import News from './Views/NewsPage.jsx';
import NewsCreate from './Views/NewsCreatePage.jsx';
import NewsEdit from './Views/NewsEditPage.jsx';
import NewsList from './Views/NewsListPage.jsx';
import Classified from './Views/ClassifiedPage.jsx';
import TopSecretList from './Views/TopSecretListPage.jsx';
import TopSecretCreate from './Views/TopSecretCreatePage.jsx';
import TopSecretEdit from './Views/TopSecretEditPage.jsx';
import Help from './Views/HelpPage.jsx';
import HelpFAQs from './Views/HelpFAQsPage.jsx';
import FAQList from './Views/FAQListPage.jsx';
import FAQCreate from './Views/FAQCreatePage.jsx';
import FAQEdit from './Views/FAQEditPage.jsx';
import HelpRequest from './Views/HelpRequestPage.jsx';
import RequestEdit from './Views/RequestEditPage.jsx';
import RequestAdminView from './Views/RequestAdminViewPage.jsx';
import HelpMyRequests from './Views/HelpMyRequestsPage.jsx';
import ConfirmationNotification from './components/ConfirmationNotification';

import { UserSettingsProvider } from './UserSettingsContext.js';
import { ActiveTabProvider } from './ActiveTabContext'; 
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Notification from './components/Notification.jsx';
import { SideMenuProvider } from './SideMenuContext.js';
import { AdminMenuProvider } from './AdminMenuContext.js';
import { ConfirmationProvider } from './ConfirmationContext.js';
import 'bootstrap/dist/css/bootstrap.min.css';

export function App(props) {

  const [notificationVisible, setNotificationVisible] = useState(false);

  const toggleNotification = () => {
    setNotificationVisible(!notificationVisible);
    setTimeout(() => {
        setNotificationVisible(false); 
      }, 10000);
  };

  return (
    <BrowserRouter >
        <UserSettingsProvider>
        <ActiveTabProvider>
        <SideMenuProvider>
        <ConfirmationProvider>
        <AdminMenuProvider>
          <div className='App' >
             {notificationVisible? <Notification />:null}
            <ConfirmationNotification toggleNotification={toggleNotification}/> 
            <Routes>
              <Route element={<Home />} path='/' />
              <Route element={<Login />} path='/login' />
              <Route element={<LoginLogo />} path='/login-logo' />
              <Route element={<CreateApp />} path='/create-app' />
              <Route element={<AdminControls />} path='/admin-controls' />
              
              <Route element={<AdminDashboard />} path='/admin-dashboard' />
              <Route element={<CharacterPortal />} path='/character-portal' />
              <Route element={<CreateCharacter />} path='/create-character' />
              <Route element={<CharacterEdit />} path='/character-edit' />
              <Route element={<RequestPortal />} path='/request-portal' />
              <Route element={<RequestAdminView />} path='/request-admin-view' />
              <Route element={<StoryItem />} path='/story-item' />
              <Route element={<CreateStoryItem />} path='/create-story-item' />

              <Route element={<EventPortal />} path='/event-portal' />
              <Route element={<NewsCreate />} path='/news-create' />
              <Route element={<NewsEdit />} path='/news-edit' />
              <Route element={<NewsList />} path='/news-list' />
              <Route element={<TopSecretList />} path='/top-secret-list' />
              <Route element={<TopSecretCreate />} path='/top-secret-create' />
              <Route element={<TopSecretEdit />} path='/top-secret-edit' />

              <Route element={<Dashboard />} path='/dashboard' />
              <Route element={<Journal />} path='/journal' />
              <Route element={<JournalLive />} path='/journal-live' />
              <Route element={<JournalEntries />} path='/journal-entries' />
              <Route element={<JournalEntryNew />} path='/new-journal-entry' />
              <Route element={<JournalEntryNew />} path='/new-journal-entry/:id' />
              <Route element={<JournalEdit />} path='/journal-edit' />

              <Route element={<Database />} path='/database' />
              <Route element={<MyItems />} path='/my-items' />
              <Route element={<StoryItemView />} path='/story-item-view' />
              <Route element={<StoryItemJournalView />} path='/story-item-journal-view' />
              <Route element={<StoryItemSearchView />} path='/story-item-search-view' />
              <Route element={<StoryItemEdit />} path='/story-item-edit' />
              <Route element={<SearchDB />} path='/searchDB' />
              <Route element={<News />} path='/news' />

              <Route element={<Classified />} path='/classified' />

              <Route element={<Help />} path='/help' />
              <Route element={<HelpFAQs />} path='/help-faqs' />
              <Route element={<FAQList />} path='/faq-list' />
              <Route element={<FAQCreate />} path='/faq-create' />
              <Route element={<FAQEdit />} path='/faq-edit' />
              <Route element={<HelpRequest />} path='/help-request' />
              <Route element={<RequestEdit />} path='/request-edit' />
              <Route element={<HelpMyRequests />} path='/help-my-requests' />

            </Routes>
          </div>
        </AdminMenuProvider>
        </ConfirmationProvider>
        </SideMenuProvider>
        </ActiveTabProvider>
        </UserSettingsProvider>
    </BrowserRouter>
  );
}
