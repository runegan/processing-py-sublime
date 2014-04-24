'''
Processing reference lookup for Sublimetext 3

Based on "chuck_doc_search.py" by
    Dealga McArdle (https://github.com/zeffii), 2013
functionality:      Opens webbrowser at Processing.org reference for the
                    highlighted keyword, if the keyword is valid.
Processing.org reference:   http://processing.org/reference

- Place this .py inside "Data/Packages/User"
- Add a shortcut to your user keymap file, e.g.;
        { "keys": ["ctrl+shift+]"], "command": "chuck_doc_search" }
- To use, make a selection of for examples "ADSR", then press your shortcut
        key(s).

'''

import sublime
import sublime_plugin
import webbrowser

keywords = ['abs_', 'acos_', 'alpha_', 'ambient_', 'ambientLight_', 'append_',
            'applyMatrix_', 'arc_', 'Array', 'arrayCopy_', 'ArrayList',
            'asin_', 'atan2_', 'atan_', 'background_', 'beginCamera_',
            'beginContour_', 'beginRaw_', 'beginRecord_', 'beginShape_',
            'bezier_', 'bezierDetail_', 'bezierPoint_', 'bezierTangent_',
            'bezierVertex_', 'binary_', 'blend_', 'blendMode_', 'blue_',
            'boolean', 'boolean_', 'box_', 'break', 'brightness_',
            'BufferedReader', 'byte', 'byte_', 'camera_', 'case', 'catch',
            'ceil_', 'char', 'char_', 'class', 'clear_', 'color', 'color_',
            'colorMode_', 'concat_', 'constrain_', 'continue', 'copy_',
            'cos_', 'createFont_', 'createGraphics_', 'createImage_',
            'createInput_', 'createOutput_', 'createReader_', 'createShape_',
            'createWriter_', 'cursor_', 'curve_', 'curveDetail_',
            'curvePoint_', 'curveTangent_', 'curveTightness_', 'curveVertex_',
            'day_', 'default', 'degrees_', 'directionalLight_',
            'displayHeight', 'displayWidth', 'dist_', 'double', 'draw_',
            'ellipse_', 'ellipseMode_', 'else', 'emissive_', 'endCamera_',
            'endContour_', 'endRaw_', 'endRecord_', 'endShape_', 'exit_',
            'exp_', 'expand_', 'extends', 'false', 'fill_', 'filter_',
            'final', 'float', 'float_', 'FloatDict', 'FloatList', 'floor_',
            'focused', 'for', 'frameCount', 'frameRate', 'frameRate_',
            'frustum_', 'get_', 'green_', 'HALF_PI', 'HashMap', 'height',
            'hex_', 'hour_', 'hue_', 'if', 'image_', 'imageMode_',
            'implements', 'import', 'int', 'int_', 'IntDict', 'IntList',
            'join_', 'JSONArray', 'JSONObject', 'key', 'keyCode',
            'keyPressed', 'keyPressed_', 'keyReleased_', 'keyTyped_', 'lerp_',
            'lerpColor_', 'lightFalloff_', 'lights_', 'lightSpecular_',
            'line_', 'loadBytes_', 'loadFont_', 'loadImage_',
            'loadJSONArray_', 'loadJSONObject_', 'loadPixels_', 'loadShader_',
            'loadShape_', 'loadStrings_', 'loadTable_', 'loadXML_', 'log_',
            'long', 'loop_', 'mag_', 'map_', 'match_', 'matchAll_', 'max_',
            'millis_', 'min_', 'minute_', 'modelX_', 'modelY_', 'modelZ_',
            'month_', 'mouseButton', 'mouseClicked_', 'mouseDragged_',
            'mouseMoved_', 'mousePressed', 'mousePressed_', 'mouseReleased_',
            'mouseWheel_', 'mouseX', 'mouseY', 'new', 'nf_', 'nfc_', 'nfp_',
            'nfs_', 'noCursor_', 'noFill_', 'noise_', 'noiseDetail_',
            'noiseSeed_', 'noLights_', 'noLoop_', 'norm_', 'normal_',
            'noSmooth_', 'noStroke_', 'noTint_', 'null', 'Object', 'open_',
            'ortho_', 'parseXML_', 'perspective_', 'PFont', 'PGraphics', 'PI',
            'PImage', 'pixels[]', 'pmouseX', 'pmouseY', 'point_',
            'pointLight_', 'popMatrix_', 'popStyle_', 'pow_', 'print_',
            'printArray_', 'printCamera_', 'println_', 'printMatrix_',
            'printProjection_', 'PrintWriter', 'private', 'PShader', 'PShape',
            'public', 'pushMatrix_', 'pushStyle_', 'PVector', 'quad_',
            'quadraticVertex_', 'QUARTER_PI', 'radians_', 'random_',
            'randomGaussian_', 'randomSeed_', 'rect_', 'rectMode_', 'red_',
            'redraw_', 'requestImage_', 'resetMatrix_', 'resetShader_',
            'return', 'reverse_', 'rotate_', 'rotateX_', 'rotateY_',
            'rotateZ_', 'round_', 'saturation_', 'save_', 'saveBytes_',
            'saveFrame_', 'saveJSONArray_', 'saveJSONObject_', 'saveStream_',
            'saveStrings_', 'saveTable_', 'saveXML_', 'scale_', 'screenX_',
            'screenY_', 'screenZ_', 'second_', 'selectFolder_',
            'selectInput_', 'selectOutput_', 'set_', 'setup_', 'shader_',
            'shape_', 'shapeMode_', 'shearX_', 'shearY_', 'shininess_',
            'shorten_', 'sin_', 'size_', 'smooth_', 'sort_', 'specular_',
            'sphere_', 'sphereDetail_', 'splice_', 'split_', 'splitTokens_',
            'spotLight_', 'sq_', 'sqrt_', 'static', 'str_', 'String',
            'StringDict', 'StringList', 'stroke_', 'strokeCap_',
            'strokeJoin_', 'strokeWeight_', 'subset_', 'super', 'switch',
            'Table', 'TableRow', 'tan_', 'TAU', 'text_', 'textAlign_',
            'textAscent_', 'textDescent_', 'textFont_', 'textLeading_',
            'textMode_', 'textSize_', 'texture_', 'textureMode_',
            'textureWrap_', 'textWidth_', 'this', 'tint_', 'translate_',
            'triangle_', 'trim_', 'true', 'try', 'TWO_PI', 'unbinary_',
            'unhex_', 'updatePixels_', 'vertex_', 'void', 'while', 'width',
            'XML', 'year_']

site = 'http://processing.org/reference/'


def findDoc(target):

    for keyword in keywords:
        if target == keyword:
            webbrowser.open(site + keyword + '.html')
            return
        # Methods in our keyword list have an underscore appended, because,
        #   on the Processing website, e.g. 'constrain' is 'constrain_'.
        elif target == keyword[0:-1]:
            webbrowser.open(site + keyword + '.html')
            return


class ProcessingRefLookup(sublime_plugin.TextCommand):
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
