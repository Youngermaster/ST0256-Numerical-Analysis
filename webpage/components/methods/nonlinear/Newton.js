import {isValidMath, mathjsToLatex, mathjsKeywords, formatLatex} from "../../utils";
import React, {useState, useEffect} from "react";
import Header from "../../header/Header";
import Graph from "../../Graph";
import * as Desmos from 'desmos';

import { addStyles, EditableMathField } from 'react-mathquill';
import { parse, derivative } from 'mathjs';
import 'katex/dist/katex.min.css';
import TeX from '@matejmazur/react-katex';

import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';
import Container from '@material-ui/core/Container';
import Divider from '@material-ui/core/Divider';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import { Alert } from '@material-ui/lab';
import Box from '@material-ui/core/Box';
import Slider from '@material-ui/core/Slider';
import Tooltip from '@material-ui/core/Tooltip';
import Fab from '@material-ui/core/Fab';
import HelpIcon from '@material-ui/icons/Help';
import Joyride, { Step as JoyrideStep, CallBackProps as JoyrideCallBackProps} from "react-joyride";
import Collapse from '@material-ui/core/Collapse';
import { Fade, Zoom, Slide } from "react-awesome-reveal";
import { useTheme } from '@material-ui/core/styles';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import { makeStyles } from '@material-ui/core/styles';



// Styles
const useStyles = makeStyles((theme) => ({
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.primary,
    margin: theme.spacing(1),
  },
  container: {
    "& > *": {
        margin: theme.spacing(1)
    }
  },
  card: {
    margin: theme.spacing(0.5),
  },
  cardContent: {
    overflow: 'auto',
    "& > *": {
        margin: theme.spacing(0.5)
    }
  },
  fab: {
    position: 'fixed',
    bottom: theme.spacing(4),
    right: theme.spacing(2),
  },
}));

addStyles(); // inserts the required css to the <head> block for mathquill

function NonlinearNewton({methodName, markdown}) {
    useEffect(() => {
        // Set webpage title
        document.title = methodName;
    });

    const styleClasses = useStyles();

    // Derivative
    // Another sample would be: `3x^2+2x-8`
    const [functionLatex, setFunctionLatex] = useState(String.raw`x-\cos\left( x\right)`);
    const [functionText, setFunctionText] = useState('');

    let functionValue, derivValue, derivLatex;
    let functionError = false;
    let functionErrorText = "";
    try {
        functionValue = parse(functionText);
        derivValue = derivative(functionText, 'x');
        derivLatex = mathjsToLatex(derivValue);
        functionValue.traverse(function (node, path, parent) {
            if (node.type === 'SymbolNode' && !mathjsKeywords.includes(node.name)) {
                if (node.name !== 'x') {
                    throw "variableName";
                }
            }
        });
    }
    catch(e) {
        functionError = true;
        functionErrorText = e === "variableName" ? "Only x variable is allowed." :  "Invalid equation!";
    }

    // Iterations
    const [iterations, setIterations] = useState(10);
    let iterError = false;
    let iterErrorText = "";
    if (!Number.isInteger(iterations) || iterations <= 0) {
        iterError = true;
        iterErrorText = "Las iteraciones deben ser positivas!";
    }

    // Initial x
    const [initialX, setInitialX] = useState(0.0);
    let initialXError = false;
    let initialXErrorText = "";
    if (isNaN(initialX)) {
        initialXError = true;
        initialXErrorText = "X inicial debe ser un numero!";
    }

    let hasError = functionError || iterError || initialXError;

    // Solve
    let solve = false;
    let results = [];
    if (isValidMath(functionValue) && !hasError) {
        solve = true;
        for (let i = 0; i < iterations; i++) {
            let previousX = (i === 0) ? initialX: results[i - 1].newX;
            let funcResult, derivResult;
            try {
                funcResult = functionValue.evaluate({x : previousX});
                derivResult = derivValue.evaluate({x : previousX});
            }
            catch {
                hasError = true;
                functionError = true;
                functionErrorText = "Solo la variable x es permitida!";
                solve = false;
                break;
            }
            
            let newX = previousX - funcResult / derivResult;
            let errorX = Math.abs(newX - previousX);
            results.push({
                previousX,
                funcResult,
                derivResult,
                newX,
                errorX,
            });
        }
    }

    // Joyride Tour
    const [runTour, setRunTour] = useState(false);
    const openHelp = () => {
        setRunTour(true);
    };
    const joyrideCallback = (state: JoyrideCallBackProps) => {
        if (state.action === "reset" || state.action === "close") {
            setRunTour(false);
        }
    };

    let params = {functionLatex, iterations, results};
    
    return (
        <>
            <Header methodName={methodName} markdown={markdown} />
            <Paper className={styleClasses.paper}>
                <Container className={styleClasses.container}>
                <Zoom duration={500} triggerOnce cascade>
                    <Grid container spacing={1} direction="row" alignItems="center" justify="center">
                        <Grid xs item className="function-input">
                            <Card className={styleClasses.card}>
                                <CardContent className={styleClasses.cardContent}>
                                    <Typography variant="h6">
                                        Funcion:
                                    </Typography>
                                    <EditableMathField
                                        disabled={false}
                                        latex={functionLatex}
                                        onChange={(mathField) => {
                                            setFunctionText(mathField.text());
                                            setFunctionLatex(mathField.latex());
                                        }}
                                        mathquillDidMount={(mathField) => {
                                            setFunctionText(mathField.text())
                                        }}
                                    />
                                </CardContent>
                            </Card>
                        </Grid>
                        <Grid xs item className="derivative-input">
                            <Card className={styleClasses.card}>
                                <CardContent className={styleClasses.cardContent}>
                                    <Typography variant="h6">
                                        Derivada:
                                    </Typography>
                                    <Collapse in={functionError}>
                                        <Alert severity="error">
                                            {functionErrorText}
                                        </Alert>
                                    </Collapse>
                                    <Collapse in={!functionError}>
                                        {!functionError && <Fade triggerOnce><TeX math={derivLatex} block /></Fade>}
                                    </Collapse>
                                </CardContent>
                            </Card>
                        </Grid>
                    </Grid>


                    <Grid container spacing={1} direction="row" alignItems="center" justify="center">
                        <Grid xs item className="iteration-input">
                            <Card className={styleClasses.card}>
                                <CardContent className={styleClasses.cardContent}>
                                    <Typography variant="h6">
                                        Iteraciones:
                                    </Typography>
                                    <TextField
                                        disabled={false}
                                        type="number"
                                        onChange={(event)=>setIterations(parseInt(event.target.value))}
                                        error={iterError}
                                        label={iterError?"Error":""}
                                        defaultValue={iterations.toString()}
                                        helperText={iterErrorText}
                                        variant="outlined"
                                    />
                                </CardContent>
                            </Card>
                        </Grid>
                        <Grid xs item className="initialX-input">
                            <Card className={styleClasses.card}>
                                <CardContent className={styleClasses.cardContent}>
                                    <Typography variant="h6">
                                        Valor inicial, <TeX math={String.raw`x_0`} />:
                                    </Typography>
                                    <TextField
                                        disabled={false}
                                        type="number"
                                        onChange={(event)=>setInitialX(parseFloat(event.target.value))}
                                        error={initialXError}
                                        label={initialXError?"Error":""}
                                        defaultValue={initialX.toString()}
                                        helperText={initialXErrorText}
                                        variant="outlined"
                                    />
                                </CardContent>
                            </Card>
                        </Grid>
                    </Grid>
                </Zoom>
                </Container>
            </Paper>

            <Divider />
            
            <Collapse in={solve}>
                <Fade triggerOnce>
                    <Paper className={styleClasses.paper}>
                        {solve && <Steps params={params}/>}
                    </Paper>
                </Fade>
            </Collapse>
            <Tooltip arrow title="Help" placement="top">
                <Fab color="secondary" aria-label="help" className={styleClasses.fab} onClick={openHelp}>
                    <HelpIcon />
                </Fab>
            </Tooltip>
           
        </>
    );
}

function Steps({params}) {

    const styleClasses = useStyles();

    const [currentIteration, setCurrentIteration] = useState(1);

    let hasError = false;
    let errorText = "";

    let results = params.results;
    let currentResult = results[currentIteration - 1];

    let latexContent, graphCallback;

    if (currentIteration > params.iterations) {
        setCurrentIteration(params.iterations);
    }
    else {
        let previousXLatex = String.raw`x_{${currentIteration - 1}}`;
        let newXLatex = String.raw`x_{${currentIteration}}`;
        latexContent =
        String.raw`
        \displaystyle
        \begin{array}{lll}
        \\ ${previousXLatex} &=& ${formatLatex(currentResult.previousX)}
        \\ f(${previousXLatex}) &=& ${formatLatex(currentResult.funcResult)}
        \\ f'(${previousXLatex}) &=& ${formatLatex(currentResult.derivResult)}
        \\ ${newXLatex} &=& ${previousXLatex} - \frac{f(${previousXLatex})}{f'(${previousXLatex})}
        \\                       &=& ${formatLatex(currentResult.newX)}
        \\ Error &=& |${newXLatex} - ${previousXLatex}|
        \\       &=& |${formatLatex(currentResult.errorX)}|
        \end{array}
        `;

        graphCallback = (calculator, currentResult) => {
            calculator.current.setExpression({ id: 'function', color: Desmos.Colors.BLUE, latex: params.functionLatex});
            calculator.current.setExpression({ id: 'derivative', color: Desmos.Colors.GREEN, lineStyle: Desmos.Styles.DOTTED, latex:
                `(y-${currentResult.funcResult})/(x-${currentResult.previousX})=${currentResult.derivResult}` });
            calculator.current.setExpression({ id: 'initialX', color: Desmos.Colors.ORANGE, pointStyle: Desmos.Styles.POINT, label: "initialX", showLabel:true, latex:
                `(${currentResult.previousX}, ${currentResult.funcResult})` });
            calculator.current.setExpression({ id: 'root', color: Desmos.Colors.RED, pointStyle: Desmos.Styles.POINT, label: "Root", showLabel:true, latex:
                `(${currentResult.newX}, 0)` });
        }
    }

    const smallScreen = useMediaQuery(useTheme().breakpoints.down('sm'));
    
    return (
        <Container className={styleClasses.container}>

            <Collapse in={hasError}>
                <Alert severity="error">
                    {errorText}
                </Alert>
            </Collapse>
            <Collapse in={!hasError}>
                <Grid className="results" container direction={smallScreen?"column":"row"} alignItems="center" justify="space-evenly">
                    <Grid xs item className="iteration-slider">
                        <Slide direction="left" triggerOnce>
                            <Box id="iteration-slider" height={smallScreen?null:"20rem"} width={smallScreen?"70vw":null}>
                                <Slider
                                    orientation={smallScreen?"horizontal":"vertical"}
                                    onChange={(event, value) => {setCurrentIteration(value)}}
                                    defaultValue={1}
                                    aria-labelledby="discrete-slider-small-steps"
                                    step={1}
                                    marks
                                    min={1}
                                    max={params.iterations}
                                    valueLabelDisplay="on"
                                />
                            </Box>
                        </Slide>
                    </Grid>
                    <Grid xs item container spacing={1} direction="column" alignItems="center" justify="center">
                        <Grid xs item className="step-math">
                            <Zoom duration={500} triggerOnce>
                                <Card className={styleClasses.card}>
                                    <CardContent className={styleClasses.cardContent}>
                                        <Typography variant="h6">
                                            Iteration {currentIteration}:
                                        </Typography>
                                        <TeX math={latexContent} block />
                                    </CardContent>
                                </Card>
                            </Zoom>
                        </Grid>
                    </Grid>
                    <Grid xs item className="graph-button">
                        <Slide direction="right" triggerOnce>
                            <Graph params={{currentIteration, graphCallback, smallScreen, ...params}} />
                        </Slide>
                    </Grid>
                </Grid>

            </Collapse>

        </Container>
    )
}

export default NonlinearNewton;