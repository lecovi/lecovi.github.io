# -*- coding: utf-8 -*-

# Copyright © 2015 Manuel Kaufmann & Leandro E. Colombo Viña

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import uuid

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from nikola.plugin_categories import RestExtension

"""Accordion and Collapse group directive for reStructuredText"""


class Plugin(RestExtension):
    """Plugin for accordion and collapse reST directive"""

    name = "accordion"

    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        directives.register_directive('accordion', Accordion)
        return super(Plugin, self).set_site(site)

CODE = """<div class="panel-group" id="{id}" role="tablist" aria-multiselectable="true">
    {content}
</div>
"""


class Accordion(Directive):
    """ reStructuredText extension for inserting collapsible groups or accordion."""

    required_arguments = 0
    optional_arguments = 999
    final_argument_whitespace = False
    option_spec = {
            }
    has_content = True

    def run(self):
        self.assert_has_content()

        text = '\n'.join(self.content)
        options = {
                'id': uuid.uuid4().hex,
                'content': text,
        }
        options.update(self.options)
        accordion_node = nodes.raw('', CODE.format(**options), format='html')

        self.state.nested_parse(self.content, self.content_offset, accordion_node)
        return [accordion_node]

