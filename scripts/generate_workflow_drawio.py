"""
generate_workflow_drawio.py
Generates:
1. experimental_workflow.drawio (Native, editable, professional draw.io flowchart)
2. paper/figures/experimental_workflow.drawio (copy)
3. Matplotlib reference rendering for fallback
"""

import os

def generate_workflow_drawio_xml(output_path):
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2026-10-11T13:30:00.000Z" agent="Antigravity" version="21.0.0" type="device">
  <diagram id="experimental-workflow" name="Experimental Workflow">
    <mxGraphModel dx="1200" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="900" pageHeight="1020" background="#FFFFFF">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- 1. Start: Terminator -->
        <mxCell id="node_start" value="&lt;b&gt;Start: Experimental Pipeline&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#5D4037&quot;&gt;DeepFake Detection under Lossy Compression&lt;/font&gt;" style="rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor=#FFE0B2;strokeColor=#E65100;strokeWidth=1.8;fontSize=11;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="320" y="25" width="260" height="50" as="geometry"/>
        </mxCell>

        <!-- 2. Dataset Ingestion: Parallelogram (Input) -->
        <mxCell id="node_ingest" value="&lt;b&gt;Dataset Ingestion (140,000 Faces)&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#5D4037&quot;&gt;Real Faces: FFHQ &amp;nbsp;|&amp;nbsp; Synthetic Faces: StyleGAN&lt;/font&gt;" style="shape=parallelogram;perimeter=parallelogramPerimeter;fixedSize=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#F57C00;strokeWidth=1.8;fontSize=11;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="300" y="105" width="300" height="52" as="geometry"/>
        </mxCell>

        <!-- Arrow: Start -> Ingest -->
        <mxCell id="edge_start_ingest" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.6;endArrow=classic;" edge="1" parent="1" source="node_start" target="node_ingest">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- 3. Data Hygiene & Partitioning: Rectangle (Process) -->
        <mxCell id="node_hygiene" value="&lt;b&gt;Data Hygiene &amp;amp; Zero-Leak Partitioning&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#424242&quot;&gt;SHA-256 &amp;amp; dHash Verified Deduplication &amp;nbsp;|&amp;nbsp; Disjoint Identity Splits&lt;br&gt;&lt;b&gt;Train:&lt;/b&gt; 7,200 &amp;nbsp;|&amp;nbsp; &lt;b&gt;Val:&lt;/b&gt; 800 &amp;nbsp;|&amp;nbsp; &lt;b&gt;Test:&lt;/b&gt; 2,000 &amp;nbsp;|&amp;nbsp; &lt;b&gt;Holdout:&lt;/b&gt; 200&lt;/font&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFF8E1;strokeColor=#FFA000;strokeWidth=1.8;fontSize=10.5;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="270" y="185" width="360" height="58" as="geometry"/>
        </mxCell>

        <!-- Arrow: Ingest -> Hygiene -->
        <mxCell id="edge_ingest_hygiene" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.6;endArrow=classic;" edge="1" parent="1" source="node_ingest" target="node_hygiene">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- 4. Stochastic Training: Rectangle (Process) -->
        <mxCell id="node_train" value="&lt;b&gt;Stochastic Compression-Aware Training&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#1B5E20&quot;&gt;&lt;b&gt;Models:&lt;/b&gt; Baseline (EfficientNet-B3) &amp;amp; Proposed (Coord-EfficientNet-B3)&lt;br&gt;p&lt;sub&gt;jpeg&lt;/sub&gt; = 0.50, QF &amp;isin; {20, 40, 50, 60, 80}, Adam (&amp;eta; = 10&lt;sup&gt;-4&lt;/sup&gt;), BCE Loss&lt;/font&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#E8F5E9;strokeColor=#2E7D32;strokeWidth=1.8;fontSize=10.5;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="250" y="270" width="400" height="62" as="geometry"/>
        </mxCell>

        <!-- Arrow: Hygiene -> Train -->
        <mxCell id="edge_hygiene_train" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.6;endArrow=classic;" edge="1" parent="1" source="node_hygiene" target="node_train">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- 5. Decision: Benchmark Regime? (Diamond) -->
        <mxCell id="node_bench" value="&lt;b&gt;Benchmark&lt;br&gt;Regime?&lt;/b&gt;" style="rhombus;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=1.8;fontSize=11;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="375" y="360" width="150" height="70" as="geometry"/>
        </mxCell>

        <!-- Arrow: Train -> Bench -->
        <mxCell id="edge_train_bench" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.6;endArrow=classic;" edge="1" parent="1" source="node_train" target="node_bench">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- Branch A: Multi-QF Testing (Table I) -->
        <mxCell id="branch_test" value="&lt;b&gt;Multi-QF Testing (Table I)&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#4A148C&quot;&gt;6 Regimes: Clean, QF80, QF60, QF50, QF40, QF20&lt;br&gt;&lt;b&gt;12,000 Total Inference Evaluations&lt;/b&gt;&lt;/font&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#EDE7F6;strokeColor=#512DA8;strokeWidth=1.8;fontSize=10.5;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="130" y="465" width="280" height="60" as="geometry"/>
        </mxCell>

        <!-- Branch B: Unseen Holdout Testing (Table II) -->
        <mxCell id="branch_holdout" value="&lt;b&gt;Unseen Holdout Testing (Table II)&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#4A148C&quot;&gt;200 Pure Facial Crops (100 Real, 100 Fake)&lt;br&gt;&lt;b&gt;1,200 Inferences Across 6 Regimes&lt;/b&gt;&lt;/font&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#EDE7F6;strokeColor=#512DA8;strokeWidth=1.8;fontSize=10.5;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="490" y="465" width="280" height="60" as="geometry"/>
        </mxCell>

        <!-- Arrow: Bench -> Branch A -->
        <mxCell id="edge_bench_test" value="&lt;b&gt;2,000 Test Set&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.6;endArrow=classic;fontSize=9.5;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="node_bench" target="branch_test">
          <mxGeometry relative="1" as="geometry">
            <Array points="270" y="395"/>
          </mxGeometry>
        </mxCell>

        <!-- Arrow: Bench -> Branch B -->
        <mxCell id="edge_bench_holdout" value="&lt;b&gt;200 Holdout&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.6;endArrow=classic;fontSize=9.5;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="node_bench" target="branch_holdout">
          <mxGeometry relative="1" as="geometry">
            <Array points="630" y="395"/>
          </mxGeometry>
        </mxCell>

        <!-- 6. Re-converge: Model Inference -->
        <mxCell id="node_infer" value="&lt;b&gt;Model Inference &amp;amp; Posterior Probability&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#5D4037&quot;&gt;Compute P(Fake | X) = &amp;sigma;(z) &amp;isin; [0, 1] for Both Models&lt;/font&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFF8E1;strokeColor=#FFA000;strokeWidth=1.8;fontSize=11;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="270" y="565" width="360" height="52" as="geometry"/>
        </mxCell>

        <!-- Arrow: Branch A -> Infer -->
        <mxCell id="edge_test_infer" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.6;endArrow=classic;" edge="1" parent="1" source="branch_test" target="node_infer">
          <mxGeometry relative="1" as="geometry">
            <Array points="270" y="545"/>
            <Array points="390" y="545"/>
          </mxGeometry>
        </mxCell>

        <!-- Arrow: Branch B -> Infer -->
        <mxCell id="edge_holdout_infer" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.6;endArrow=classic;" edge="1" parent="1" source="branch_holdout" target="node_infer">
          <mxGeometry relative="1" as="geometry">
            <Array points="630" y="545"/>
            <Array points="510" y="545"/>
          </mxGeometry>
        </mxCell>

        <!-- 7. Decision: Classification Rule (Diamond) -->
        <mxCell id="node_rule" value="&lt;b&gt;Classification Rule&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#D84315&quot;&gt;P(Fake | X) &amp;ge; &amp;tau;?&lt;/font&gt;" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFDE7;strokeColor=#FBC02D;strokeWidth=1.8;fontSize=11;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="360" y="650" width="180" height="70" as="geometry"/>
        </mxCell>

        <!-- Arrow: Infer -> Rule -->
        <mxCell id="edge_infer_rule" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.6;endArrow=classic;" edge="1" parent="1" source="node_infer" target="node_rule">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- Rule: No -> Real (0) -->
        <mxCell id="label_real" value="&lt;b style=&quot;color:#1B5E20;&quot;&gt;Real (0)&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#333333&quot;&gt;P &amp;lt; &amp;tau;&lt;/font&gt;" style="rounded=1;arcSize=20;whiteSpace=wrap;html=1;fillColor=#E8F5E9;strokeColor=#2E7D32;strokeWidth=1.5;fontSize=10.5;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="180" y="660" width="110" height="48" as="geometry"/>
        </mxCell>

        <!-- Rule: Yes -> Fake (1) -->
        <mxCell id="label_fake" value="&lt;b style=&quot;color:#B71C1C;&quot;&gt;Fake (1)&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#333333&quot;&gt;P &amp;ge; &amp;tau;&lt;/font&gt;" style="rounded=1;arcSize=20;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#C62828;strokeWidth=1.5;fontSize=10.5;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="610" y="660" width="110" height="48" as="geometry"/>
        </mxCell>

        <!-- Arrow: Rule -> Real -->
        <mxCell id="edge_rule_real" value="&lt;b&gt;No&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#2E7D32;strokeWidth=1.6;endArrow=classic;fontSize=10;labelBackgroundColor=#FFFFFF;fontColor=#2E7D32;" edge="1" parent="1" source="node_rule" target="label_real">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- Arrow: Rule -> Fake -->
        <mxCell id="edge_rule_fake" value="&lt;b&gt;Yes&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#C62828;strokeWidth=1.6;endArrow=classic;fontSize=10;labelBackgroundColor=#FFFFFF;fontColor=#C62828;" edge="1" parent="1" source="node_rule" target="label_fake">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- 8. Statistical Validation: Parallelogram (Output) -->
        <mxCell id="node_stats" value="&lt;b&gt;Statistical Validation &amp;amp; Tabular Results Generation&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#01579B&quot;&gt;&lt;b&gt;Table I:&lt;/b&gt; Multi-QF Benchmark &amp;nbsp;|&amp;nbsp; &lt;b&gt;Table II:&lt;/b&gt; Unseen Holdout (-49.1% Errors)&lt;br&gt;&lt;b&gt;Table III:&lt;/b&gt; Threshold Optimization (&amp;tau; &amp;isin; [0.15, 0.50]) &amp;nbsp;|&amp;nbsp; &lt;b&gt;McNemar Test:&lt;/b&gt; p = 0.00116 (&lt; 0.01)&lt;/font&gt;" style="shape=parallelogram;perimeter=parallelogramPerimeter;fixedSize=1;whiteSpace=wrap;html=1;fillColor=#E1F5FE;strokeColor=#0288D1;strokeWidth=1.8;fontSize=10.5;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="200" y="760" width="500" height="60" as="geometry"/>
        </mxCell>

        <!-- Arrow: Rule -> Stats -->
        <mxCell id="edge_rule_stats" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.6;endArrow=classic;" edge="1" parent="1" source="node_rule" target="node_stats">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- 9. End: Terminator -->
        <mxCell id="node_end" value="&lt;b&gt;End: Robust Detection Validated&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#1B5E20&quot;&gt;14.4% Compressed Error Reduction Confirmed&lt;/font&gt;" style="rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor=#C8E6C9;strokeColor=#2E7D32;strokeWidth=1.8;fontSize=11;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="310" y="860" width="280" height="48" as="geometry"/>
        </mxCell>

        <!-- Arrow: Stats -> End -->
        <mxCell id="edge_stats_end" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#37474F;strokeWidth=1.6;endArrow=classic;" edge="1" parent="1" source="node_stats" target="node_end">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(xml_content.strip())
    print(f"Generated clean native draw.io flowchart at: {output_path}")

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

def generate_workflow_png(output_path):
    fig, ax = plt.subplots(figsize=(7.5, 9.2), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 122)
    ax.axis('off')

    c_text_dark = '#212121'

    def draw_card(x, y, w, h, title, lines, bg, border, shape='rect', skew=3.0):
        if shape == 'rect':
            box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2,rounding_size=1.2",
                                 facecolor=bg, edgecolor=border, linewidth=1.6)
            ax.add_patch(box)
        elif shape == 'oval':
            box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2,rounding_size=3.5",
                                 facecolor=bg, edgecolor=border, linewidth=1.8)
            ax.add_patch(box)
        elif shape == 'parallelogram':
            pts = [
                [x + skew, y + h],
                [x + w + skew, y + h],
                [x + w - skew, y],
                [x - skew, y]
            ]
            poly = Polygon(pts, closed=True, facecolor=bg, edgecolor=border, linewidth=1.6)
            ax.add_patch(poly)

        cx = x + w / 2
        if title and not lines:
            ax.text(cx, y + h / 2, title, ha='center', va='center',
                    fontsize=8.8, fontweight='bold', color=c_text_dark)
        elif title:
            ax.text(cx, y + h - 2.5, title, ha='center', va='center',
                    fontsize=8.8, fontweight='bold', color=c_text_dark)
            curr_y = y + h - 5.0
            for line in lines:
                ax.text(cx, curr_y, line, ha='center', va='center',
                        fontsize=7.6, color='#37474F')
                curr_y -= 2.4

    def draw_diamond(cx, cy, w, h, text1, text2, bg, border):
        pts = [
            [cx, cy + h / 2],
            [cx + w / 2, cy],
            [cx, cy - h / 2],
            [cx - w / 2, cy]
        ]
        poly = Polygon(pts, closed=True, facecolor=bg, edgecolor=border, linewidth=1.6)
        ax.add_patch(poly)
        ax.text(cx, cy + 1.2, text1, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=c_text_dark)
        ax.text(cx, cy - 1.5, text2, ha='center', va='center',
                fontsize=7.6, color='#5D4037')

    def draw_arrow(x1, y1, x2, y2, label="", label_pos='center', color='#263238'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.5, mutation_scale=10))
        if label:
            lx = (x1 + x2) / 2
            ly = (y1 + y2) / 2 + 1.0
            ax.text(lx, ly, label, ha='center', va='bottom',
                    fontsize=7.6, fontweight='bold', color=color,
                    bbox=dict(boxstyle='square,pad=0.15', fc='white', ec='none'))

    # 1. Start: Terminator
    draw_card(27, 113, 46, 7, "Start: Experimental Pipeline", [
        "DeepFake Detection under Lossy Compression"
    ], '#FFE0B2', '#E65100', shape='oval')
    draw_arrow(50, 113, 50, 108.5)

    # 2. Dataset Ingestion: Parallelogram
    draw_card(25, 101.5, 50, 7, "Dataset Ingestion (140,000 Faces)", [
        "Real Faces: FFHQ  |  Synthetic Faces: StyleGAN"
    ], '#FFF3E0', '#F57C00', shape='parallelogram', skew=2.5)
    draw_arrow(50, 101.5, 50, 97)

    # 3. Data Hygiene & Partitioning
    draw_card(20, 88.5, 60, 8.5, "Data Hygiene & Zero-Leak Partitioning", [
        "SHA-256 & dHash Verified Deduplication | Disjoint Identities",
        "Train: 7,200 | Val: 800 (Clean) | Test: 2,000 | Holdout: 200"
    ], '#FFF8E1', '#FFA000')
    draw_arrow(50, 88.5, 50, 84)

    # 4. Stochastic Compression-Aware Training
    draw_card(18, 75, 64, 9, "Stochastic Compression-Aware Training", [
        "Models: Baseline (EfficientNet-B3) & Proposed (Coord-EfficientNet-B3)",
        "p_jpeg = 0.50, QF ∈ {20, 40, 50, 60, 80}, Adam (lr = 1e-4), BCE Loss"
    ], '#E8F5E9', '#2E7D32')
    draw_arrow(50, 75, 50, 70)

    # 5. Benchmark Decision: Diamond
    draw_diamond(50, 65, 24, 9.5, "Benchmark", "Regime?", '#E3F2FD', '#1976D2')

    # Parallel branches
    # Branch A: Multi-QF
    draw_card(5, 50, 42, 8, "Multi-QF Testing (Table I)", [
        "6 Regimes: Clean, QF80, QF60, QF50, QF40, QF20",
        "12,000 Total Inference Evaluations"
    ], '#EDE7F6', '#512DA8')

    # Branch B: Unseen Holdout
    draw_card(53, 50, 42, 8, "Unseen Holdout Testing (Table II)", [
        "200 Pure Facial Crops (100 Real, 100 Fake)",
        "1,200 Inferences Across 6 Regimes"
    ], '#EDE7F6', '#512DA8')

    # Arrows from Diamond to Branches
    ax.plot([38, 26, 26], [65, 65, 58], color='#263238', lw=1.5)
    draw_arrow(26, 58, 26, 58, label="2,000 Test Set")

    ax.plot([62, 74, 74], [65, 65, 58], color='#263238', lw=1.5)
    draw_arrow(74, 58, 74, 58, label="200 Holdout")

    # 6. Re-converge: Model Inference
    draw_card(22, 38, 56, 7.5, "Model Inference & Posterior Probability", [
        "Compute P(Fake | X) = σ(z) ∈ [0, 1] for Both Models"
    ], '#FFF8E1', '#FFA000')

    # Arrows from Branches to Model Inference
    ax.plot([26, 26, 42], [50, 47, 47], color='#263238', lw=1.5)
    draw_arrow(42, 47, 42, 45.5)

    ax.plot([74, 74, 58], [50, 47, 47], color='#263238', lw=1.5)
    draw_arrow(58, 47, 58, 45.5)

    # 7. Decision: Classification Rule
    draw_diamond(50, 27.5, 26, 9.5, "Classification Rule", "P(Fake | X) ≥ τ?", '#FFFDE7', '#FBC02D')
    draw_arrow(50, 38, 50, 32.25)

    # Decisions: Real / Fake
    draw_card(8, 24.5, 18, 6, "Real (0)", ["P < τ"], '#E8F5E9', '#2E7D32')
    draw_arrow(37, 27.5, 26, 27.5, label="No", color='#2E7D32')

    draw_card(74, 24.5, 18, 6, "Fake (1)", ["P ≥ τ"], '#FFEBEE', '#C62828')
    draw_arrow(63, 27.5, 74, 27.5, label="Yes", color='#C62828')

    # 8. Statistical Validation: Parallelogram
    draw_card(15, 12, 70, 7.5, "Statistical Validation & Tabular Generation", [
        "Table I: Multi-QF  |  Table II: Holdout (-49.1% Err)  |  McNemar (p < 0.01)"
    ], '#E1F5FE', '#0288D1', shape='parallelogram', skew=2.5)
    draw_arrow(50, 22.75, 50, 19.5)

    # 9. End: Terminator
    draw_card(27, 2, 46, 6.5, "End: Robust Detection Validated", [
        "14.4% Compressed Error Reduction Confirmed"
    ], '#C8E6C9', '#2E7D32', shape='oval')
    draw_arrow(50, 12, 50, 8.5)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    pdf_path = output_path.replace('.png', '.pdf')
    plt.savefig(pdf_path, bbox_inches='tight')
    plt.close()
    print(f"Generated clean workflow PNG at: {output_path} and PDF at: {pdf_path}")

if __name__ == '__main__':
    generate_workflow_drawio_xml("experimental_workflow.drawio")
    generate_workflow_drawio_xml("paper/figures/experimental_workflow.drawio")
    generate_workflow_png("paper/figures/experimental_workflow.png")
    generate_workflow_png("paper/experimental_workflow.png")
    print("All experimental workflow files generated successfully!")

