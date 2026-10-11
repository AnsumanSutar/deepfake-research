"""
generate_drawio_and_diagram.py
1. Generates an authentic, fully editable .drawio XML file for draw.io (app.diagrams.net).
2. Generates an ultra-clear, publication-grade architecture block diagram PNG (300 DPI)
   for the research paper.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

def generate_drawio_xml(output_path):
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2026-10-11T11:20:00.000Z" agent="Antigravity" version="21.0.0" type="device">
  <diagram id="coord-efficientnet-b3" name="Coord-EfficientNet-B3 Architecture">
    <mxGraphModel dx="1400" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="900" background="#FFFFFF">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Title -->
        <mxCell id="title" value="&lt;b&gt;Coord-EfficientNet-B3: Proposed DeepFake Detection Architecture&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=18;fontColor=#1A237E;" vertex="1" parent="1">
          <mxGeometry x="380" y="20" width="650" height="30" as="geometry"/>
        </mxCell>

        <!-- 1. Input Image Block -->
        <mxCell id="input_box" value="&lt;b&gt;Input Facial Image&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#555555&quot;&gt;RGB Face Crop&lt;br&gt;224 &amp;times; 224 &amp;times; 3&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1F5FE;strokeColor=#0288D1;strokeWidth=2;fontSize=12;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="40" y="200" width="130" height="90" as="geometry"/>
        </mxCell>

        <!-- 2. Backbone Feature Extractor -->
        <mxCell id="backbone_box" value="&lt;b&gt;EfficientNet-B3 Backbone&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#424242&quot;&gt;ImageNet Pre-trained&lt;br&gt;Stem + MBConv Stages 1&amp;ndash;7&lt;br&gt;&lt;b&gt;Output Feature Map:&lt;/b&gt;&lt;br&gt;F &amp;isin; &amp;reals;&lt;sup&gt;1536 &amp;times; 7 &amp;times; 7&lt;/sup&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8EAF6;strokeColor=#3F51B5;strokeWidth=2;fontSize=11;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="220" y="185" width="170" height="120" as="geometry"/>
        </mxCell>

        <!-- Arrow: Input -> Backbone -->
        <mxCell id="edge1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=2;endArrow=classic;endFill=1;" edge="1" parent="1" source="input_box" target="backbone_box">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- 3. Coordinate Attention Group (Container) -->
        <mxCell id="coord_container" value="&lt;b style=&quot;font-size: 13px; color: #004D40;&quot;&gt;Proposed Coordinate Attention (CoordAtt) Module&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E0F2F1;strokeColor=#00796B;strokeWidth=2;strokeDashed=1;verticalAlign=top;align=center;spacingTop=10;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="440" y="80" width="530" height="330" as="geometry"/>
        </mxCell>

        <!-- Sub 3A: X-AvgPool -->
        <mxCell id="pool_h" value="&lt;b&gt;X-AvgPool (1D)&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#333333&quot;&gt;Pool W &amp;rarr; 1&lt;br&gt;&lt;b&gt;z&lt;sup&gt;h&lt;/sup&gt;&lt;/b&gt; &amp;isin; &amp;reals;&lt;sup&gt;1536 &amp;times; 7 &amp;times; 1&lt;/sup&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#00897B;strokeWidth=1.5;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="470" y="130" width="130" height="60" as="geometry"/>
        </mxCell>

        <!-- Sub 3B: Y-AvgPool -->
        <mxCell id="pool_w" value="&lt;b&gt;Y-AvgPool (1D)&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#333333&quot;&gt;Pool H &amp;rarr; 1&lt;br&gt;&lt;b&gt;z&lt;sup&gt;w&lt;/sup&gt;&lt;/b&gt; &amp;isin; &amp;reals;&lt;sup&gt;1536 &amp;times; 1 &amp;times; 7&lt;/sup&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#00897B;strokeWidth=1.5;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="470" y="270" width="130" height="60" as="geometry"/>
        </mxCell>

        <!-- Sub 3C: Shared 1x1 Conv + BN + Hard-Swish -->
        <mxCell id="shared_conv" value="&lt;b&gt;Concat &amp;amp; Shared 1&amp;times;1 Conv&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#333333&quot;&gt;Batch Normalization&lt;br&gt;Hard-Swish Activation&lt;br&gt;Reduction Ratio r = 32&lt;br&gt;&lt;b&gt;1536 &amp;rarr; 48 channels&lt;/b&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#00897B;strokeWidth=1.5;fontSize=10.5;" vertex="1" parent="1">
          <mxGeometry x="640" y="190" width="150" height="80" as="geometry"/>
        </mxCell>

        <!-- Sub 3D: Split & Sigmoid (H) -->
        <mxCell id="conv_h" value="&lt;b&gt;Split &amp;amp; 1&amp;times;1 Conv&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#333333&quot;&gt;Sigmoid Activation&lt;br&gt;&lt;b&gt;g&lt;sup&gt;h&lt;/sup&gt;&lt;/b&gt; &amp;isin; &amp;reals;&lt;sup&gt;1536 &amp;times; 7 &amp;times; 1&lt;/sup&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#00897B;strokeWidth=1.5;fontSize=10.5;" vertex="1" parent="1">
          <mxGeometry x="830" y="130" width="120" height="60" as="geometry"/>
        </mxCell>

        <!-- Sub 3E: Split & Sigmoid (W) -->
        <mxCell id="conv_w" value="&lt;b&gt;Split &amp;amp; 1&amp;times;1 Conv&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#333333&quot;&gt;Sigmoid Activation&lt;br&gt;&lt;b&gt;g&lt;sup&gt;w&lt;/sup&gt;&lt;/b&gt; &amp;isin; &amp;reals;&lt;sup&gt;1536 &amp;times; 1 &amp;times; 7&lt;/sup&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#00897B;strokeWidth=1.5;fontSize=10.5;" vertex="1" parent="1">
          <mxGeometry x="830" y="270" width="120" height="60" as="geometry"/>
        </mxCell>

        <!-- Sub 3F: Feature Modulation -->
        <mxCell id="mod_box" value="&lt;b&gt;Coordinate Modulation&lt;/b&gt;&lt;br&gt;&lt;b&gt;Y = F &amp;otimes; g&lt;sup&gt;h&lt;/sup&gt; &amp;otimes; g&lt;sup&gt;w&lt;/sup&gt;&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#2E7D32&quot;&gt;Y &amp;isin; &amp;reals;&lt;sup&gt;1536 &amp;times; 7 &amp;times; 7&lt;/sup&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#C8E6C9;strokeColor=#2E7D32;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="645" y="330" width="140" height="60" as="geometry"/>
        </mxCell>

        <!-- Arrows inside CoordAtt -->
        <mxCell id="edge_f_to_poolh" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.8;endArrow=classic;" edge="1" parent="1" source="backbone_box" target="pool_h">
          <mxGeometry relative="1" as="geometry">
            <Array points="420" y="245"/>
            <Array points="420" y="160"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge_f_to_poolw" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.8;endArrow=classic;" edge="1" parent="1" source="backbone_box" target="pool_w">
          <mxGeometry relative="1" as="geometry">
            <Array points="420" y="245"/>
            <Array points="420" y="300"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge_poolh_to_shared" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.5;endArrow=classic;" edge="1" parent="1" source="pool_h" target="shared_conv">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge_poolw_to_shared" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.5;endArrow=classic;" edge="1" parent="1" source="pool_w" target="shared_conv">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge_shared_to_h" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.5;endArrow=classic;" edge="1" parent="1" source="shared_conv" target="conv_h">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge_shared_to_w" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.5;endArrow=classic;" edge="1" parent="1" source="shared_conv" target="conv_w">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge_gh_to_mod" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.5;endArrow=classic;" edge="1" parent="1" source="conv_h" target="mod_box">
          <mxGeometry relative="1" as="geometry">
            <Array points="970" y="160"/>
            <Array points="970" y="360"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge_gw_to_mod" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.5;endArrow=classic;" edge="1" parent="1" source="conv_w" target="mod_box">
          <mxGeometry relative="1" as="geometry">
            <Array points="890" y="360"/>
          </mxGeometry>
        </mxCell>

        <!-- 4. Global Average Pooling -->
        <mxCell id="gap_box" value="&lt;b&gt;Global Average&lt;br&gt;Pooling (GAP)&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#4A148C&quot;&gt;&lt;b&gt;y&#772;&lt;/b&gt; &amp;isin; &amp;reals;&lt;sup&gt;1536&lt;/sup&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#7B1FA2;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1010" y="200" width="110" height="90" as="geometry"/>
        </mxCell>

        <!-- Arrow: Mod Box -> GAP -->
        <mxCell id="edge_mod_to_gap" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=2;endArrow=classic;" edge="1" parent="1" source="mod_box" target="gap_box">
          <mxGeometry relative="1" as="geometry">
            <Array points="1040" y="360"/>
            <Array points="1040" y="245"/>
          </mxGeometry>
        </mxCell>

        <!-- 5. Classifier Head Container -->
        <mxCell id="head_container" value="&lt;b style=&quot;color: #B71C1C;&quot;&gt;3-Stage Classifier Head&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#C62828;strokeWidth=2;strokeDashed=1;verticalAlign=top;align=center;spacingTop=8;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1150" y="160" width="160" height="170" as="geometry"/>
        </mxCell>

        <mxCell id="fc1" value="Dense 1536 &amp;rarr; 128&lt;br&gt;ReLU + Dropout (0.3)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E53935;strokeWidth=1;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="1165" y="195" width="130" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="fc2" value="Dense 128 &amp;rarr; 64&lt;br&gt;ReLU + Dropout (0.2)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E53935;strokeWidth=1;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="1165" y="240" width="130" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="fc3" value="Dense 64 &amp;rarr; 1 (Logit z)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E53935;strokeWidth=1;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="1165" y="285" width="130" height="30" as="geometry"/>
        </mxCell>

        <!-- Arrow: GAP -> Classifier Head -->
        <mxCell id="edge_gap_to_head" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=2;endArrow=classic;" edge="1" parent="1" source="gap_box" target="fc1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- 6. Output Decision Box -->
        <mxCell id="decision_box" value="&lt;b&gt;Classification Decision&lt;/b&gt;&lt;br&gt;&lt;b&gt;P(Fake | X) = &amp;sigma;(z)&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#333333&quot;&gt;Decision Threshold &amp;tau;&lt;/font&gt;&lt;br&gt;&lt;font color=&quot;#1B5E20&quot;&gt;&amp;tau; &amp;lt; 0.50 &amp;rarr; &lt;b&gt;Real&lt;/b&gt;&lt;/font&gt;&lt;br&gt;&lt;font color=&quot;#B71C1C&quot;&gt;&amp;tau; &amp;ge; 0.50 &amp;rarr; &lt;b&gt;Fake&lt;/b&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF9C4;strokeColor=#F57F17;strokeWidth=2;fontSize=10.5;" vertex="1" parent="1">
          <mxGeometry x="1350" y="195" width="140" height="100" as="geometry"/>
        </mxCell>

        <!-- Arrow: FC3 -> Decision -->
        <mxCell id="edge_fc_to_decision" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=2;endArrow=classic;" edge="1" parent="1" source="fc3" target="decision_box">
          <mxGeometry relative="1" as="geometry">
            <Array points="1320" y="300"/>
            <Array points="1320" y="245"/>
          </mxGeometry>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(xml_content.strip())
    print(f"Generated draw.io XML file at: {output_path}")

def generate_clean_block_diagram_png(output_path):
    fig, ax = plt.subplots(figsize=(11, 5.8), dpi=300)
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 60)
    ax.axis('off')

    # Palette
    c_input_bg = '#E1F5FE'
    c_input_border = '#0288D1'

    c_backbone_bg = '#E8EAF6'
    c_backbone_border = '#3F51B5'

    c_coord_bg = '#E0F2F1'
    c_coord_border = '#00796B'
    c_sub_bg = '#FFFFFF'

    c_gap_bg = '#F3E5F5'
    c_gap_border = '#7B1FA2'

    c_head_bg = '#FFEBEE'
    c_head_border = '#C62828'

    c_decision_bg = '#FFF9C4'
    c_decision_border = '#F57F17'

    c_text = '#212121'

    def draw_card(x, y, w, h, title, lines, bg, border, dashed=False, lw=1.6):
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2,rounding_size=1.5",
                             facecolor=bg, edgecolor=border, linewidth=lw,
                             linestyle='--' if dashed else '-')
        ax.add_patch(box)
        if title:
            ax.text(x + w/2, y + h - 2.8, title, ha='center', va='center',
                    fontsize=9.5, fontweight='bold', color=c_text)
        curr_y = y + h - 5.5 if title else y + h/2 + 1.2 * (len(lines)-1)
        for line in lines:
            ax.text(x + w/2, curr_y, line, ha='center', va='center',
                    fontsize=8, color='#37474F')
            curr_y -= 2.8

    def draw_arrow(x1, y1, x2, y2, label=""):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>", color='#263238', lw=1.6, mutation_scale=12))
        if label:
            ax.text((x1+x2)/2, (y1+y2)/2 + 1.2, label, ha='center', va='bottom',
                    fontsize=7.5, fontweight='bold', color='#1A237E')

    # 1. Input Image
    draw_card(2, 23, 13, 14, "Input Image", [
        "Face Crop",
        "$224 \\times 224 \\times 3$"
    ], c_input_bg, c_input_border)
    draw_arrow(15, 30, 19, 30)

    # 2. Backbone Feature Extractor
    draw_card(19, 20, 16, 20, "EfficientNet-B3\nBackbone", [
        "ImageNet Pre-trained",
        "Stem + MBConv 1-7",
        "Feature Map $F$:",
        "$\\mathbb{R}^{1536 \\times 7 \\times 7}$"
    ], c_backbone_bg, c_backbone_border)
    draw_arrow(35, 30, 39, 30, "$F$")

    # 3. Coordinate Attention Group (Container)
    coord_box = FancyBboxPatch((39, 6), 39, 48, boxstyle="round,pad=0.4,rounding_size=2.0",
                               facecolor=c_coord_bg, edgecolor=c_coord_border, linewidth=2.0, linestyle='--')
    ax.add_patch(coord_box)
    ax.text(58.5, 51.5, "Proposed Coordinate Attention Module", ha='center', va='center',
            fontsize=10.5, fontweight='bold', color='#004D40')

    # Sub-blocks inside Coordinate Attention
    # (A) 1D Horizontal Pool
    draw_card(41, 37, 14, 9, "X-AvgPool (1D)", [
        "Pool $W \\to 1$",
        "$z^h \\in \\mathbb{R}^{1536 \\times 7 \\times 1}$"
    ], c_sub_bg, c_coord_border)

    # (B) 1D Vertical Pool
    draw_card(41, 17, 14, 9, "Y-AvgPool (1D)", [
        "Pool $H \\to 1$",
        "$z^w \\in \\mathbb{R}^{1536 \\times 1 \\times 7}$"
    ], c_sub_bg, c_coord_border)

    # (C) Shared 1x1 Conv + BN + Hard-Swish
    draw_card(60, 26, 16, 12, "Shared 1x1 Conv\nBN + Hard-Swish", [
        "Reduction $r=32$",
        "$1536 \\to 48$ channels"
    ], c_sub_bg, c_coord_border)

    # (D) Split Convs & Sigmoids
    draw_card(60, 10, 16, 10, "Split 1x1 Convs\n& Sigmoid ($g^h, g^w$)", [
        "$48 \\to 1536$ channels"
    ], c_sub_bg, c_coord_border)

    # (E) Modulation
    draw_card(41, 8.5, 14, 6, "Modulation", [
        "$Y = F \\otimes g^h \\otimes g^w$"
    ], '#C8E6C9', '#2E7D32')

    # Connectors inside CoordAtt
    draw_arrow(35, 30, 41, 41.5)
    draw_arrow(35, 30, 41, 21.5)
    draw_arrow(55, 41.5, 60, 33)
    draw_arrow(55, 21.5, 60, 29)
    draw_arrow(68, 26, 68, 20)
    draw_arrow(60, 12, 55, 12)

    # Output from CoordAtt to GAP
    ax.plot([41, 38, 38, 80, 80], [11.5, 11.5, 3, 3, 30], color='#263238', lw=1.6)
    draw_arrow(80, 30, 82, 30)
    ax.text(58.5, 4.5, "Modulated Feature Representation $Y \\in \\mathbb{R}^{1536 \\times 7 \\times 7}$",
            ha='center', va='center', fontsize=7.8, color='#1B5E20', fontweight='bold')

    # 4. Global Average Pooling
    draw_card(82, 23, 8.5, 14, "GAP", [
        "Global Avg",
        "Pooling",
        "$\\bar{y} \\in \\mathbb{R}^{1536}$"
    ], c_gap_bg, c_gap_border)
    draw_arrow(90.5, 30, 93, 30)

    # 5. Classifier Head
    draw_card(93, 17, 10, 26, "Classifier\nHead", [
        "Dense 1536→128",
        "(ReLU, p=0.3)",
        "↓",
        "Dense 128→64",
        "(ReLU, p=0.2)",
        "↓",
        "Dense 64→1",
        "Logit $z$"
    ], c_head_bg, c_head_border)
    draw_arrow(103, 30, 105, 30)

    # 6. Decision
    draw_card(105, 22, 12, 16, "Decision", [
        "Sigmoid $\\sigma(z)$",
        "$P(\\text{Fake}) \\in [0, 1]$",
        "Threshold $\\tau$",
        "$\\geq 0.50 \\rightarrow$ Fake",
        "$< 0.50 \\rightarrow$ Real"
    ], c_decision_bg, c_decision_border)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated clean architecture block diagram at: {output_path}")

if __name__ == '__main__':
    # Generate draw.io files in paper/figures and root
    generate_drawio_xml("paper/figures/architecture_proposed_model.drawio")
    generate_drawio_xml("architecture_proposed_model.drawio")
    
    # Generate clean PNG
    generate_clean_block_diagram_png("paper/figures/architecture_block_diagram.png")
