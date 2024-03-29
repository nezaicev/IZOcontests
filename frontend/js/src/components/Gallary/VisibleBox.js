import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import useInfiniteScroll from "../hooks/useInfiniteScroll";
import axios from "axios";
import {CircularProgress} from "@mui/material";


export default function VisibleBox(props) {
    const [items, setItems] = useState([])
    const [isFetching, setIsFetching] = useState(false);
    const [HasMore, setHasMore] = useState(true);


    const [lastElementRef] = useInfiniteScroll(
        HasMore ? loadMoreItems : () => {
        },
        isFetching
    );
    useEffect(() => {

        if (props.nomination) {
            setItems([])
            props.setPage(1, loadMoreItems())

        }
    }, [props.nomination])

    function loadMoreItems() {

        setIsFetching(true);
        axios({
            method: "GET",
            url: props.url,
            params: {
                page_size: 1,
                publish: true,
                contest_name: props.contestName,
                year: props.year,
                page: props.page,
                nomination: props.nomination,
                // theme:props.theme,
                ordering: '-rating',
            },
        })
            .then((res) => {
                setItems((prevTitles) => {
                    return [...new Set([...prevTitles, ...res.data.results.map((b) => b)])];
                });
                props.setPage((prevPageNumber) => prevPageNumber + 1);
                setHasMore(!!res.data.next);
                setIsFetching(false);
            })
            .catch((e) => {
                console.log(e);
            });
    }


    return (
        <Box>

            { items.length===0?'':props.visualComponent(items, lastElementRef)}

              {isFetching && <Box sx={{
                justifyContent: 'center',
                height: '600',
                display: 'flex',
                  marginTop:' 20px'
            }}>
                <CircularProgress  sx={{
                    color:'#d26666'
                }}/>
            </Box>}
        </Box>
    )
}

