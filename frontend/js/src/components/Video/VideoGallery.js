import axios from "axios";
import React, {useEffect, useState} from "react";
import useInfiniteScroll from "../hooks/useInfiniteScroll";
import Box from "@mui/material/Box";
import HorizontalTabs from "../Gallary/HorizontalTabs";
import {CircularProgress, Grid} from "@mui/material";
import VideoItem from "./VideoItem";


function VideoGallery(props) {
    const [page, setPage] = React.useState(1)
    const [data, setData] = React.useState([])
    const [isFetching, setIsFetching] = useState(false);
    const [HasMore, setHasMore] = useState(true);

    const [lastElementRef] = useInfiniteScroll(
        HasMore ? loadMoreItems : () => {
        },
        isFetching
    );

    function loadMoreItems(dataInitial, pageInitial) {

        setIsFetching(true);
        axios({
            method: "GET",
            url: `${process.env.REACT_APP_HOST_NAME}/frontend/api/video/`,
            params: {
                page_size: 3,
                section: props.section,
                page: pageInitial ? 1 : page,
            },
        })
            .then((res) => {
                setData((prevTitles) => {
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

    useEffect(() => {
        setPage(1)
        setData([])
        loadMoreItems(null, 1)

    }, [])


    return (
        <>

            <Box>
                <Grid container spacing={2}
                      sx={{justifyContent: 'space-between'}}>
                    {data.map((item, index) => (
                        item['link'] ?
                            <Grid item xs="auto" key={index}
                                  ref={(data.length === index + 1) ? lastElementRef : null}>
                                <VideoItem link={item['link']} title={item['title']}
                                           description={item['description']}/>
                            </Grid> : ''
                    ))}

                </Grid>
                {isFetching && <Box sx={{
                    justifyContent: 'center',
                    height: '600',
                    display: 'flex',
                    marginTop: ' 20px'
                }}>
                    <CircularProgress sx={{
                        color: '#d26666'
                    }}/>
                </Box>}
            </Box>


        </>
    )
}


export {VideoGallery}