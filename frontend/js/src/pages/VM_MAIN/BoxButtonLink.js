import React from "react";

const BoxButtonLink = (props) => {
    return (
        <a href={props.href} style={{
            fill: props.color,
            transition: '0.5s',
            cursor: props.active ? 'hand' : 'default',
        }}
           onMouseEnter={(e) => {
               if (props.active) {
                   e.currentTarget.style.fill = '#fff'
               }
           }}
           onMouseLeave={(e) => {
               if (props.active) {
                   e.currentTarget.style.fill = props.color
               }
           }}>
            {props.children}

        </a>
    )
}

export {BoxButtonLink}