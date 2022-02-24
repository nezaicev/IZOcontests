import ImageList from "@material-ui/core/ImageList";
import React, {useEffect, useState} from "react";
import axios from 'axios';
import {video} from "../data/video";
import PlayerModal from "./PlayerModal";
import useInfiniteScroll from "../src/useInfiniteScroll";
import Box from "@material-ui/core/Box";
import CircularProgress from "@material-ui/core/CircularProgress";




export default function VideoGallery() {

    //we change here
    const [Items, setItems] = useState([]);
    const [isFetching, setIsFetching] = useState(false);
    //setting tha initial page
    const [page, setPage] = useState(1);
    //we need to know if there is more data
    const [HasMore, setHasMore] = useState(true);

    const [lastElementRef] = useInfiniteScroll(
        HasMore ? loadMoreItems : () => {},
        isFetching
    );
    //on initial mount
    useEffect(() => {
        loadMoreItems();
    }, []);
    function loadMoreItems() {
        setIsFetching(true);

        //using axios to access the third party API
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/frontend/api/archive",
            params: { page_size: 1, contest_name:'mymoskvichi', status:5, page:page },
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
        <ImageList sx={{width: 350, height: 250}} cols={3} rowHeight={250}>

            {Items.map((item, index) => {
                if (Items.length === index + 1) {

                    return (
                        //referencing the last item to be watched by the observer

                        <PlayerModal name={item.author_name} url={item.link}  key={index} forwardedRef={lastElementRef}>
                            {item} - <b>last</b>
                        </PlayerModal>

                    );
                } else {
                    return <PlayerModal name={item.author_name} url={item.link} key={index}/>



                }
            })}
            {isFetching &&  <Box sx={{ display: 'flex' }}>
                <CircularProgress />
            </Box>}


        </ImageList>
    )

}