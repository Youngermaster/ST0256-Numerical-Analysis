import { lazy } from 'react';

// Markdown
import NonlinearBisectionMarkdown from '../components/methods/nonlinear/markdown/bisection.md';
import NonlinearFalsePositionMarkdown from '../components/methods/nonlinear/markdown/falsePosition.md';
import NonlinearFixedPointMarkdown from '../components/methods/nonlinear/markdown/fixedPoint.md';
import NonlinearNewtonMarkdown from '../components/methods/nonlinear/markdown/newton.md';
import NonlinearSecantMarkdown from '../components/methods/nonlinear/markdown/secant.md';



// JSX Components
const NonlinearBisection = lazy(() => import('../components/methods/nonlinear/Bisection'));
const NonlinearFalsePosition = lazy(() => import('../components/methods/nonlinear/FalsePosition'));
const NonlinearNewton = lazy(() => import('../components/methods/nonlinear/Newton'));
const NonlinearSecant = lazy(() => import('../components/methods/nonlinear/Secant'));
const NonlinearFixedPoint = lazy(() => import('../components/methods/nonlinear/FixedPoint'));



const categories = [
    {
        name : "Raices de ecuaciones",
        path : "nonlinear",
        methods : [
            {
                name: "Biseccion",
                path : "bisection",
                component: NonlinearBisection,
                completed: true,
                markdown: NonlinearBisectionMarkdown,
            },
            {
                name: "Regula falsi",
                path : "false_position",
                component: NonlinearFalsePosition,
                completed: true,
                markdown: NonlinearFalsePositionMarkdown,
            },
            {
                name: "Punto fijo",
                path : "fixed_point",
                component: NonlinearFixedPoint,
                completed: true,
                markdown: NonlinearFixedPointMarkdown,
            },
            {
                name: "Newton Raphson",
                path: "newton",
                component: NonlinearNewton,
                completed: true,
                markdown: NonlinearNewtonMarkdown,
            },
            {
                name: "Secante modificada",
                path : "secant",
                component: NonlinearSecant,
                completed: true,
                markdown: NonlinearSecantMarkdown,
            },
        ]
    },
   

]

export default categories;