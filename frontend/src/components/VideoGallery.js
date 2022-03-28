
import React, {useEffect, useState} from "react";
import axios from 'axios';
import PlayerModal from "./PlayerModal";
import useInfiniteScroll from "../useInfiniteScroll";
import Box from "@material-ui/core/Box";
import CircularProgress from "@material-ui/core/CircularProgress";
import {ImageListStyled} from "../styled";


export default function VideoGallery() {

    const [Items, setItems] = useState([]);
    const [isFetching, setIsFetching] = useState(false);

    const [page, setPage] = useState(1);

    const [HasMore, setHasMore] = useState(true);

    const [lastElementRef] = useInfiniteScroll(
        HasMore ? loadMoreItems : () => {
        },
        isFetching
    );

    useEffect(() => {
        loadMoreItems();
    }, []);

    function loadMoreItems() {
        setIsFetching(true);


        axios({
            method: "GET",
            url: `http://${process.env.REACT_APP_HOST_NAME}/frontend/api/archive`,
            params: {page_size: 1, contest_name: 'mymoskvichi', status: 5, page: page},
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
        <ImageListStyled sx={{justifyContent:'center'}} cols={3} rowHeight={250}>

            {Items.map((item, index) => {
                if (Items.length === index + 1) {

                    return (

                        <PlayerModal name={item.author_name} url={item.link} key={index} forwardedRef={lastElementRef}>
                        </PlayerModal>

                    );
                } else {
                    return <PlayerModal name={item.author_name} url={item.link} key={index}/>


                }
            })}
            {isFetching && <Box sx={{display: 'flex'}}>
                <CircularProgress/>
            </Box>}


        </ImageListStyled>
    )

}