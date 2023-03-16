import './App.css';
import React from "react";
import {Router, Route, Routes,BrowserRouter, Navigate} from 'react-router-dom'
import GalleryPageVP from "./pages/VP/GalleryPageVP";
import GalleryPageArtakiada from "./pages/ARTAKIADA/GalleryPageArtakiada";
import GallaryPageNRusheva from "./pages/NRUSHEVA/GallaryPageNRusheva";
import GalleryPageMyMoskvichi
    from "./pages/MYMOSKVICHI/GalleryPageMyMoskvichi";
import MainPage from "./pages/MAIN/MainPage";
import EventPage from "./pages/EVENT/EventPage";
import BroadcastListPage from "./pages/BROADCAST/BroadcastListPage";
import BroadcastPage from "./pages/BROADCAST/BroadcastPage";
import ExpositionListPage from "./pages/EXPOSITION/ExpositionListPage";
import ExpositionPage from "./pages/EXPOSITION/ExpositionPage";
import BasePage from "./components/BasePage/BasePage";
import Statistics from "./pages/STATISTICS/Statistics";
import MymoskvichiMainPage from "./pages/MYMOSKVICHI/MymoskvichiMainPage";
import GalleryPageDesign from "./pages/DESIGN/GalleryPageDesign";

const host = process.env.REACT_APP_HOST_NAME

const App = () => {
    return (
        <>
            <BrowserRouter>

                <Routes>

                    <Route path='/frontend/main/' element={<MainPage/>}/>
                    <Route path='/frontend/vp/' element={<GalleryPageVP/>}/>
                    <Route path='/frontend/design/' element={<GalleryPageDesign/>}/>
                    <Route path='/frontend/artakiada/' element={<GalleryPageArtakiada/>}/>
                    <Route path='/frontend/nrusheva/' element={<GallaryPageNRusheva/>}/>
                    <Route path='/frontend/mymoskvichi/:slug/' element={<MymoskvichiMainPage/>}/>
                    <Route path='/frontend/test/' element={<GalleryPageMyMoskvichi/>}/>

                    <Route path='/frontend/event/:id/' element={<EventPage/>} />
                    <Route path='/frontend/broadcasts/' element={<BroadcastListPage/>} />
                    <Route path='/frontend/broadcast/:id/' element={<BroadcastPage/>} />
                    <Route path='/frontend/expositions/' element={<ExpositionListPage/>}/>
                    <Route path='/frontend/exposition/:id/' element={<ExpositionPage/>}/>
                    <Route path='/frontend/page/:slug/' element={<BasePage/>}/>
                    <Route path='/frontend/page/statistics/' element={<Statistics/>}/>


                </Routes>
                {/*<Switch>*/}
                {/*     <Route path='/frontend/event/:id/' children={<EventPage/>} />*/}
                {/*</Switch>*/}

            </BrowserRouter>

        </>


    );
}
export default App