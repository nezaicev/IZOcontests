import Card from "@material-ui/core/Card";
import React, {useEffect, useState} from "react";
import {styled} from "@mui/material/styles";
import useInfiniteScroll from "../useInfiniteScroll";
import axios from "axios";
import Box from "@material-ui/core/Box";
import CircularProgress from "@material-ui/core/CircularProgress";
import { ExpandMoreCollapse} from "./ExpandMore";

import ScrollableTabs from "./ScrollableTabs";
import {ImageButton} from "../styled";
import ImageListItem from "@material-ui/core/ImageListItem";
import Tooltip from "@material-ui/core/Tooltip";
import IconButton from "@material-ui/core/IconButton";
import OndemandVideoIcon from "@mui/icons-material/OndemandVideo";





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
                page_size: 9,
                publish:true,
                contest_name: props.contestName,
                page: page,
                theme: (theme === 'Все') ? '' : theme
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
                <ScrollableTabs url={`http://${process.env.REACT_APP_HOST_NAME}/frontend/api/archive/theme/artakiada`}
                                loadData={loadMoreItems}
                                resetPage={resetPage}

                                resetLoadedData={() => {
                                    setItems([]);
                                }}
                                setTheme={(value) => {
                                    setTheme(value);

                                }}

                />
            </Box>

            {Items.map((item, index) => {
                if (Items.length === index + 1) {

                    return (
                        <ImageButton sx={{
                    p: '10px',
                    backgroundColor: '#ffffff'
                }} >

                      <ImageListItem  key={index}>
                          lastElementRef={lastElementRef}
                                <a href={item['image']['original']}>
                                    <img
                                        src={item['image']['thumb']}
                                        alt={item['author_name']}
                                        loading="lazy"

                                    />

                                </a>
                            </ImageListItem>

                </ImageButton>

                    );
                } else {
                    return (
                            <ImageButton sx={{
                    p: '10px',
                    backgroundColor: '#ffffff'
                }} >

                      <ImageListItem  key={index}>
                          lastElementRef={lastElementRef}
                                <a href={item['image']['original']}>
                                    <img
                                        src={item['image']['thumb']}
                                        alt={item['author_name']}
                                        loading="lazy"

                                    />

                                </a>
                            </ImageListItem>

                </ImageButton>

                    )


                }
            })}
            {isFetching && <Box sx={{justifyContent: 'center', height:'600', display:'flex'}}>
                <CircularProgress/>
            </Box>}
        </Box>
    )
}