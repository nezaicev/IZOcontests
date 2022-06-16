import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import useInfiniteScroll from "../../hooks/useInfiniteScroll";
import axios from "axios";
import MixCard from "../MixCard";
import {ExpandMoreCollapse} from "./ExpandMore";


export default function VisibleBoxVP(props) {
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
            {items.map((item, index) => {
                if (items.length === index + 1) {

                    return (<MixCard sx={{
                        boxShadow: 0,
                        // border: 2.5,
                        // borderColor: '#b7b6b6'
                    }} key={index} ref={lastElementRef}>
                        <ExpandMoreCollapse item={item} index={index}
                                            key={index}/>
                    </MixCard>)

                } else {
                    return (<MixCard sx={{
                        boxShadow: 0,
                        // border: 2.5,
                        // borderColor: '#b7b6b6',
                        // backgroundColor:'rgba(243,227,227,0.45)'
                    }} key={index}>
                        <ExpandMoreCollapse item={item} index={index}
                                            key={index}/>
                    </MixCard>)
                }


            })}
        </Box>
    )
}

