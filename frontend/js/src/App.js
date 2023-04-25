import './App.css';
import React from "react";
import {Router, Route, Routes, BrowserRouter, Navigate, Link} from 'react-router-dom'
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
import MymoskvichiMainPage from "./pages/MYMOSKVICHI/MymoskvichiMainPage";
import GalleryPageDesign from "./pages/DESIGN/GalleryPageDesign";
import {Contests} from "./pages/MAIN/Contests";
import {Layout} from "./components/BasePage/Layout";
import {Events} from "./pages/EVENT/Events";
import {Broadcasts} from "./pages/BROADCAST/Broadcasts";
import {Expositions} from "./pages/EXPOSITION/Expositions";
import {Archive} from "./pages/EXPOSITION/Archive";
import {Statistics} from './pages/EXPOSITION/Statistics'

const host = process.env.REACT_APP_HOST_NAME

const App = () => {
    return (
        <>
            <BrowserRouter>

                <Routes>
                    <Route path='/' element={<Layout tabs={[
                        {'name': 'Конкурсы', 'link': '/contests'},
                        {'name': 'Мероприятия', 'link': '/events'},
                        {'name': 'Вебинары', 'link': '/broadcasts'},
                        {'name': 'Выставки', 'link': '/expositions/main'},
                        // {'name': 'Виртуальный музей', 'link': 'http://shkola-nemenskogo.ru/'}

                    ]}/>}>
                        <Route index element={<Contests/>}/>
                        <Route path='contests' element={<Contests/>}/>
                        <Route path='events' element={<Events/>}/>
                        <Route path='broadcasts' element={<Broadcasts/>}/>

                    </Route>


                    <Route path='/expositions' element={<Layout tabs={[
                        {'name': 'Главная', 'link': '/'},
                        {'name': 'Выставки', 'link': '/expositions/main'},
                        {'name': 'Архив', 'link': '/expositions/archive'},
                        {'name': 'Статистика', 'link': '/expositions/statistics'},

                    ]}/>}>
                        <Route index element={<Expositions/>}/>
                        <Route path='main' element={<Expositions/>}/>
                        <Route path='archive' element={<Archive/>}/>
                        <Route path='statistics' element={<Statistics/>}/>


                    </Route>
                </Routes>





                    {/*<Route path='/' element={<MainPage/>}/>*/}
                    {/*<Route path='/frontend/vp/' element={<GalleryPageVP/>}/>*/}
                    {/*<Route path='/frontend/design/' element={<GalleryPageDesign/>}/>*/}
                    {/*<Route path='/frontend/artakiada/' element={<GalleryPageArtakiada/>}/>*/}
                    {/*<Route path='/frontend/nrusheva/' element={<GallaryPageNRusheva/>}/>*/}
                    {/*<Route path='/frontend/mymoskvichi/:slug/' element={<MymoskvichiMainPage/>}/>*/}
                    {/*<Route path='/frontend/test/' element={<GalleryPageMyMoskvichi/>}/>*/}
                    {/*<Route path='/frontend/event/:id/' element={<EventPage/>} />*/}
                    {/*<Route path='/frontend/broadcasts/' element={<BroadcastListPage/>} />*/}
                    {/*<Route path='/frontend/broadcast/:id/' element={<BroadcastPage/>} />*/}
                    {/*<Route path='/frontend/expositions/' element={<ExpositionListPage/>}/>*/}
                    {/*<Route path='/frontend/exposition/:id/' element={<ExpositionPage/>}/>*/}
                    {/*<Route path='/frontend/page/:slug/' element={<BasePage/>}/>*/}
                    {/*<Route path='/frontend/page/statistics/' element={<Statistics/>}/>*/}

            </BrowserRouter>

        </>


    );
}
export default App