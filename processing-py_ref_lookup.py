'''
Processing.py reference lookup for Sublimetext 3

Based on "chuck_doc_search.py" by
    Dealga McArdle (https://github.com/zeffii), 2013
functionality:      Opens webbrowser at Processing.py reference for the
                    highlighted keyword, if the keyword is valid.
Processing.py reference:   http://py.processing.org/reference

- Place this .py inside "Data/Packages/User"
- Add a shortcut to your user keymap file, e.g.;
        { "keys": ["ctrl+shift+]"], "command": "processing_ref_lookup" }
- To use, make a selection of for examples "ADSR", then press your shortcut
        key(s).

'''

import sublime
import sublime_plugin
import webbrowser

keywords = ['abs', 'acos', 'alpha', 'ambient', 'ambientLight',
            'applyMatrix', 'arc', 'asin', 'atan2', 'atan', 'background',
            'beginCamera', 'beginContour', 'beginRaw', 'beginRecord',
            'beginShape', 'bezier', 'bezierDetail', 'bezierPoint',
            'bezierTangent', 'bezierVertex', 'binary', 'blend', 'blendMode',
            'blue', 'Boolean', 'box', 'break', 'brightness', 'BufferedReader',
            'camera', 'catch', 'ceil', 'class', 'clear', 'color', 'colorMode',
            'concat', 'constrain', 'continue', 'copy', 'cos', 'createFont',
            'createGraphics', 'createImage', 'createInput', 'createOutput',
            'createReader', 'createShape', 'createWriter', 'cursor', 'curve',
            'curveDetail', 'curvePoint', 'curveTangent', 'curveTightness',
            'curveVertex', 'day', 'degrees', 'directionalLight',
            'displayHeight', 'displayWidth', 'dist', 'draw', 'ellipse',
            'ellipseMode', 'else', 'emissive', 'endCamera', 'endContour',
            'endRaw', 'endRecord', 'endShape', 'exit', 'exp', 'False', 'fill',
            'filter', 'float', 'floatconvert', 'floor', 'focused', 'for',
            'frameCount', 'frameRate', 'frameRate_var', 'frustum', 'get',
            'green', 'HALF_PI', 'HashMap', 'height', 'hex', 'hour', 'hue',
            'if', 'image', 'imageMode', 'int', 'int_convert', 'join',
            'JSONArray', 'JSONObject', 'key', 'keyCode', 'keyPressed_var',
            'keyPressed', 'keyReleased', 'keyTyped', 'lerp', 'lerpColor',
            'lightFalloff', 'lights', 'lightSpecular', 'line', 'loadBytes',
            'loadFont', 'loadImage', 'loadJSONArray', 'loadJSONObject',
            'loadPixels', 'loadShader', 'loadShape', 'loadStrings',
            'loadTable', 'loadXML', 'log', 'loop', 'mag', 'map', 'match',
            'matchAll', 'max', 'millis', 'min', 'minute', 'modelX', 'modelY',
            'modelZ', 'month', 'mouseButton', 'mouseClicked', 'mouseDragged',
            'mouseMoved', 'mousePressed', 'mousePressed_var', 'mouseReleased',
            'mouseWheel', 'mouseX', 'mouseY', 'new', 'nf', 'nfc', 'nfp',
            'nfs', 'noCursor', 'noFill', 'noise', 'noiseDetail', 'noiseSeed',
            'noLights', 'noLoop', 'norm', 'normal', 'noSmooth', 'noStroke',
            'noTint', 'Object', 'ortho', 'parseXML', 'perspective', 'PFont',
            'PGraphics', 'PI', 'PImage', 'pixels', 'pmouseX', 'pmouseY',
            'point', 'pointLight', 'popMatrix', 'popStyle', 'pow', 'print',
            'printArray', 'printCamera', 'println', 'printMatrix',
            'printProjection', 'PrintWriter', 'PShader', 'PShape',
            'pushMatrix', 'pushStyle', 'PVector', 'quad', 'quadraticVertex',
            'QUARTER_PI', 'radians', 'random', 'randomGaussian', 'randomSeed',
            'rect', 'rectMode', 'red', 'redraw', 'requestImage',
            'resetMatrix', 'resetShader', 'return', 'reverse', 'rotate',
            'rotateX', 'rotateY', 'rotateZ', 'round', 'saturation', 'save',
            'saveBytes', 'saveFrame', 'saveJSONArray', 'saveJSONObject',
            'saveStream', 'saveStrings', 'saveTable', 'saveXML', 'scale',
            'screenX', 'screenY', 'screenZ', 'second', 'selectFolder',
            'selectInput', 'selectOutput', 'set', 'setup', 'shader', 'shape',
            'shapeMode', 'shearX', 'shearY', 'shininess', 'shorten', 'sin',
            'size', 'smooth', 'list_sort', 'specular', 'sphere',
            'sphereDetail', 'splice', 'split', 'splitTokens', 'spotLight',
            'sq', 'sqrt', 'static', 'strconvert', 'string', 'stroke',
            'strokeCap', 'strokeJoin', 'strokeWeight', 'super', 'tan', 'TAU',
            'text', 'textAlign', 'textAscent', 'textDescent', 'textFont',
            'textLeading', 'textMode', 'textSize', 'texture', 'textureMode',
            'textureWrap', 'textWidth', 'tint', 'translate', 'triangle',
            'True', 'TWO_PI', 'unbinary', 'unhex', 'updatePixels', 'vertex',
            'while', 'width', 'XML', 'year']

site = 'http://py.processing.org/reference/'


def findDoc(target):

    for keyword in keywords:
        if target == keyword:
            webbrowser.open(site + keyword + '.html')
            return
        # Methods in our keyword list have an underscore appended, because,
        #   on the Processing website, e.g. 'constrain' is 'constrain'.
        elif target == keyword[0:-1]:
            webbrowser.open(site + keyword + '.html')
            return


class ProcessingPyRefLookup(sublime_plugin.TextCommand):
    def run(self, edit):
        if not self.enabled():
            tmsg = 'Please select a keyword'
            sublime.status_message(tmsg)
            return

        view = self.view
        sel = view.sel()[0]
        target = view.substr(sel)
        findDoc(target)

    def enabled(self):
        '''only allow 1 selection for version 0.1'''

        sels = self.view.sel()    # lists regions,
        nsels = len(sels)          # dir(sels[0]) for methods
        fsel = sels[0]            # first selection

        if nsels == 1 and not fsel.empty():
            return True
