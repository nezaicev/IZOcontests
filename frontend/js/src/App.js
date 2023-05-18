import './App.css';
import React from "react";
import {Router, Route, Routes, BrowserRouter, Navigate, Link} from 'react-router-dom'

import {Contests} from "./pages/MAIN/Contests";
import {Layout} from "./components/BasePage/Layout";
import {Events} from "./pages/EVENT/Events";
import {Broadcasts} from "./pages/BROADCAST/Broadcasts";
import {Expositions} from "./pages/EXPOSITION/Expositions";
import {Archive} from "./pages/EXPOSITION/Archive";
import {Statistics} from './pages/EXPOSITION/Statistics'
import {TextContent} from "./components/TextContent";
import GalleryVP from "./components/Gallary/VP/GalleryVP";
import GalleryArtakiada from "./components/Gallary/Artakiada/GalleryArtakiada";
import GalleryNRusheva from "./components/Gallary/NRusheva/GalleryNRusheva";

import {TextContentMymoskvichi} from "./pages/MYMOSKVICHI/TextContentMymoskvichi";
import GalleryMyMoskvichi from "./components/Gallary/MyMoskvichi/GalleryMyMoskvichi";
import Event from "./pages/EVENT/Event";
import Broadcast from "./pages/BROADCAST/Broadcast";
import {ContestsStatistics} from "./pages/STATISTICS/ContestsStatistics";
import {Exposition} from "./pages/EXPOSITION/Exposition";



const host = process.env.REACT_APP_HOST_NAME

const App = () => {
    return (
        <>
            <BrowserRouter>

                <Routes>


                    {/*'_______Главная________'*/}
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

                    {/*'____Выставки______'*/}
                    <Route path='/expositions' element={<Layout tabs={[
                        // {'name': 'Главная', 'link': '/'},
                        {'name': 'Выставки', 'link': '/expositions/main'},
                        {'name': 'Архив', 'link': '/expositions/archive'},
                        {'name': 'Статистика', 'link': '/expositions/statistics'},

                    ]}/>}>
                        <Route index element={<Expositions isArchive={0}/>}/>
                        <Route path='main' element={<Expositions isArchive={0}/>}/>
                        <Route path='archive' element={<Archive isArchive={1}/>}/>
                        <Route path='statistics' element={<Statistics/>}/>

                    </Route>

                    {/*'______Временные редиректы______'*/}
                    <Route path="frontend/vp/" element={<Navigate to="/vp/gallery"  />} />
                    <Route path="frontend/artakiada/" element={<Navigate to="/artakiada/gallery"  />} />
                    <Route path="frontend/nrusheva/" element={<Navigate to="/nrusheva/gallery"  />} />
                    <Route path="frontend/mymoskvichi/2/" element={<Navigate to="/mymoskvichi/gallery"  />} />
                    <Route path="frontend/mymoskvichi/0/" element={<Navigate to="/mymoskvichi"  />} />
                    <Route path="frontend/mymoskvichi/" element={<Navigate to="/mymoskvichi"  />} />
                     <Route path="frontend/expositions/" element={<Navigate to="/expositions"  />} />


                    {/*'______Худ. проекты______'*/}
                    <Route path='/vp' element={<Layout tabs={[
                        {'name': 'Художественные проекты', 'link': '/vp'},
                        {'name': 'Положение', 'link': '/vp/statute'},
                        {'name': 'Галерея', 'link': '/vp/gallery'},


                    ]}/>}>
                        <Route index
                               element={<TextContent link={'/frontend/api/page/vp_base_info/'}/>}/>
                        <Route path='statute'
                               element={<TextContent link={'/frontend/api/page/vp_pologenie/'}/>}/>
                        <Route path='gallery' element={<GalleryVP
                            contestName={process.env.REACT_APP_VP}
                            urlVerticalTabs={`${host}/frontend/api/archive/contest/years/`}
                            urlHorizontalTabs={`${host}/frontend/api/archive/contest/nominations/`}
                            urlContent={`${host}/frontend/api/archive/`}
                        />}/>

                    </Route>

                    {/*'______Артакиада____'*/}
                    <Route path='/artakiada' element={<Layout tabs={[
                        {'name': 'АРТакиада', 'link': '/artakiada'},
                        {'name': 'Положение', 'link': '/artakiada/statute'},
                        {'name': 'Галерея', 'link': '/artakiada/gallery'},

                    ]}/>}>
                        <Route index
                               element={<TextContent
                                   link={'/frontend/api/page/artakiada_base_info/'}/>}/>
                        <Route path='statute'
                               element={<TextContent
                                   link={'/frontend/api/page/artakiada_pologenie/'}/>}/>
                        <Route path='gallery' element={
                            <GalleryArtakiada
                                contestName={process.env.REACT_APP_ARTAKIADA}
                                urlVerticalTabs={`${host}/frontend/api/archive/contest/years/`}
                                urlHorizontalTabs={`${host}/frontend/api/archive/contest/thems/`}
                                urlCreativeTack={`${host}/frontend/api/contest/creative_tack/`}
                                urlContent={`${host}/frontend/api/archive/`}>
                            </GalleryArtakiada>
                        }/>

                    </Route>

                    {/*'______Н.Рушева____'*/}
                    <Route path='/nrusheva' element={<Layout tabs={[
                        {'name': 'Конкурс им. Нади Рушевой', 'link': '/nrusheva'},
                        {'name': 'Положение', 'link': '/nrusheva/statute'},
                        {'name': 'Галерея', 'link': '/nrusheva/gallery'},

                    ]}/>}>
                        <Route index
                               element={<TextContent
                                   link={'/frontend/api/page/nrusheva_base_info/'}/>}/>
                        <Route path='statute'
                               element={<TextContent
                                   link={'/frontend/api/page/nrusheva_pologenie/'}/>}/>
                        <Route path='gallery' element={

                            <GalleryNRusheva
                                contestName={process.env.REACT_APP_NRUSHEVA}
                                urlVerticalTabs={`${host}/frontend/api/archive/contest/years/`}
                                urlHorizontalTabs={`${host}/frontend/api/archive/contest/thems/`}
                                urlCreativeTack={`${host}/frontend/api/contest/creative_tack/`}
                                urlContent={`${host}/frontend/api/archive/`}>
                            </GalleryNRusheva>
                        }/>

                    </Route>

                    {/*'______МыМосквичи____'*/}
                    <Route path='/mymoskvichi' element={<Layout tabs={[
                        {'name': 'Мы Москвичи', 'link': '/mymoskvichi'},
                        {'name': 'Положение', 'link': '/mymoskvichi/statute'},
                        {'name': 'Галерея', 'link': '/mymoskvichi/gallery'},
                        {'name': 'Жюри', 'link': '/mymoskvichi/mymoskvichi_gury'}

                    ]}/>}>
                        <Route index
                               element={<TextContentMymoskvichi
                                   link={'/frontend/api/page/mymoskvichi_base_info/'}/>}/>
                        <Route path='statute'
                               element={<TextContent
                                   link={'/frontend/api/page/mymoskvichi_pologenie/'}/>}/>
                        <Route path='mymoskvichi_gury'
                               element={<TextContent
                                   link={'/frontend/api/page/mymoskvichi_gury/'}/>}/>

                        <Route path='gallery' element={

                            <GalleryMyMoskvichi
                                contestName={process.env.REACT_APP_MYMOSKVICHI}
                                urlVerticalTabs={`${host}/frontend/api/archive/contest/years/`}
                                urlHorizontalTabs={`${host}/frontend/api/archive/contest/nominations/`}
                                urlContent={`${host}/frontend/api/archive/`}>
                            </GalleryMyMoskvichi>
                        }/>

                    </Route>

                    {/*'_______Мероприятие________'*/}
                    <Route path='/' element={<Layout tabs={[
                        {'name': 'Мероприятия', 'link': '/event'},
                    ]}/>}>
                        <Route path='event/:id' element={<Event/>}/>
                        <Route path="frontend/event/:id" element={<Navigate to="/events"  />} />
                    </Route>

                    {/*'_______Трансляция________'*/}
                    <Route path='/' element={<Layout tabs={[
                        {'name': 'Трансляция', 'link': '/broadcast'},
                    ]}/>}>
                        <Route path='broadcast/:id' element={<Broadcast/>}/>
                        <Route path="frontend/broadcast/:id" element={<Navigate to="/broadcasts"  />} />
                    </Route>

                    {/*'_______Выставка________'*/}
                    <Route path='exposition/' element={<Layout tabs={[
                        {'name': 'Выставка', 'link': '/exposition'},
                    ]}/>}>
                        <Route path=':id/' element={<Exposition/>}/>
                    </Route>

                    {/*'_______Статистика________'*/}
                    <Route path='/' element={<Layout tabs={[
                        {'name': 'Статистика', 'link': '/statistics'},
                    ]}/>}>
                        <Route path='statistics' element={<ContestsStatistics/>}/>
                    </Route>


                </Routes>


            </BrowserRouter>

        </>


    );
}
export default App