
import React, {useEffect, useState} from "react";
import useInfiniteScroll from "../useInfiniteScroll";
import axios from "axios";
import Box from "@mui/material/Box";
import CircularProgress from "@mui/material/CircularProgress";
import HorizontalTabs from "./HorizontalTabs";
import SimpleReactLightbox, {SRLWrapper} from "simple-react-lightbox";
import {ItemImage} from "./ItemImage";
import {createLabel} from "../utils";



const options = {
    settings: {
        autoplaySpeed: 3000,
        boxShadow: 'none',
        disableKeyboardControls: false,
        disablePanzoom: false,
        disableWheelControls: false,
        hideControlsAfter: false,
        lightboxTransitionSpeed: 0.3,
        lightboxTransitionTimingFunction: 'linear',
        overlayColor: 'rgb(38 30 27 /98%)',
        slideAnimationType: 'fade',
        slideSpringValues: [300, 50],
        slideTransitionSpeed: 0.6,
        slideTransitionTimingFunction: 'linear',
        usingPreact: false
    },
    buttons: {
        backgroundColor: "rgb(104 99 97)",
        iconColor: "#dcd9d9",
    },
    caption: {
        captionColor: "#ffffff",
        fontFamily: "Roboto",
        captionContainerPadding: '0px 0 0px 0',
        showCaption: true

    },
    thumbnails: {
        showThumbnails: false
    }

};


export default function ImageGalleryFetch(props) {


    const [Items, setItems] = useState([]);
    const [isFetching, setIsFetching] = useState(false);
    const [page, setPage] = useState(1);
    const [theme, setTheme] = useState('');

    const [HasMore, setHasMore] = useState(true);

    const [lastElementRef] = useInfiniteScroll(
        HasMore ? loadMoreItems : () => {
        },
        isFetching
    );

    const resetPage = () => {
        setPage((value) => {
            return 1
        });

    }


    function loadMoreItems() {
        setIsFetching(true);

        axios({
            method: "GET",
            url: `http://${process.env.REACT_APP_HOST_NAME}/frontend/api/archive/`,
            params: {
                page_size: 3,
                publish: true,
                contest_name: props.contestName,
                page: page,
                theme: (theme === 'Все') ? '' : theme,
                ordering:'-rating',
            },
        })
            .then((res) => {
                setItems((prevTitles) => {
                    return [...new Set([...prevTitles, ...res.data.results.map((b) => b)])];
                });
                setPage((prevPageNumber) => prevPageNumber + 1);
                setHasMore(!!res.data.next);
                setIsFetching(false);
            })
            .catch((e) => {
                console.log(e);
            });
    }


    return (
        <Box>
            <Box sx={{margin: '20px', width: 'auto'}}>
                <HorizontalTabs
                    url={props.urlTheme}
                    loadData={loadMoreItems}
                    resetPage={resetPage}

                    resetLoadedData={() => {
                        setItems([]);
                    }}
                    setNomination={(value) => {
                        setTheme(value);

                    }}

                />
            </Box>

            <Box sx={{
                marginTop: '10px',
                marginLeft: 'auto',
                marginRight: 'auto',
                width: [250, 500, 1100]
                , display: 'block',
            }}>
                <SimpleReactLightbox>
                    <SRLWrapper options={options}>
                        {Items.map((item, index) => {
                            if (Items.length === index + 1) {

                                return (
                                    <ItemImage image={item.image} key={index} label={createLabel(item)}
                                               lastElementRef={lastElementRef}/>

                                );
                            } else {
                                return (
                                    <ItemImage image={item.image} key={index} label={createLabel(item)}/>
                                )


                            }
                        })}
                    </SRLWrapper>
                </SimpleReactLightbox>

            </Box>


            {isFetching && <Box sx={{
                justifyContent: 'center',
                height: '600',
                display: 'flex'
            }}>
                <CircularProgress/>
            </Box>}
        </Box>
    )
}