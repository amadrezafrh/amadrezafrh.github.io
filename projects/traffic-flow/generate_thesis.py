#!/usr/bin/env python3
"""Generate Bachelor Thesis PDF for Traffic Flow project."""

import os
from fpdf import FPDF

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(BASE))


class ThesisPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(120, 120, 120)
            self.cell(0, 10, "Deep Learning-Based Vehicle Detection and Traffic Flow Analysis", align="C")
            self.ln(5)
            self.set_draw_color(180, 180, 180)
            self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
            self.ln(5)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-20)
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(120, 120, 120)
            self.cell(0, 10, str(self.page_no()), align="C")

    def chapter_title(self, num, title):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(0, 0, 0)
        self.ln(5)
        self.cell(0, 10, f"{num}. {title}", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(60, 60, 60)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(6)

    def sub_title(self, num, title):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(30, 30, 30)
        self.ln(3)
        self.cell(0, 8, f"{num} {title}", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def body_text(self, text):
        self.set_font("Helvetica", "", 11)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 6.5, text)
        self.ln(3)

    def bold_text(self, text):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 6.5, text)
        self.ln(3)

    def math_text(self, text):
        self.set_font("Courier", "", 11)
        self.set_text_color(0, 0, 0)
        self.cell(0, 8, text, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def bullet(self, text):
        self.set_font("Helvetica", "", 11)
        self.set_text_color(30, 30, 30)
        x = self.get_x()
        self.cell(8, 6.5, "-")
        self.multi_cell(0, 6.5, text)
        self.ln(1)

    def add_figure(self, img_path, caption, max_w=150):
        if not os.path.exists(img_path):
            self.body_text(f"[Image not found: {img_path}]")
            return
        self.ln(3)
        from PIL import Image as PILImage
        img = PILImage.open(img_path)
        w, h = img.size
        ratio = h / w
        display_w = min(max_w, self.w - self.l_margin - self.r_margin)
        display_h = display_w * ratio
        # Check if figure fits on current page
        if self.get_y() + display_h + 20 > self.h - 25:
            self.add_page()
        x = (self.w - display_w) / 2
        self.image(img_path, x=x, w=display_w)
        self.ln(3)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, caption, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(30, 30, 30)
        self.ln(5)

    def ref_item(self, tag, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        x = self.get_x()
        self.set_font("Helvetica", "B", 10)
        self.cell(12, 6, f"[{tag}]")
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 6, text)
        self.ln(2)


def build_pdf():
    pdf = ThesisPDF()
    pdf.set_margins(25, 25, 25)

    # ---- COVER PAGE ----
    pdf.add_page()
    pdf.ln(15)
    logo = os.path.join(ROOT, "icons", "iust.png")
    if os.path.exists(logo):
        x = (pdf.w - 50) / 2
        pdf.image(logo, x=x, w=50)
    pdf.ln(10)

    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Iran University of Science and Technology", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, "Department of Electrical and Computer Engineering", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(20)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "Bachelor of Science Thesis", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(8)
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 12, "Deep Learning-Based Vehicle Detection\nand Traffic Flow Analysis", align="C")

    pdf.ln(20)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 8, "Author", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Ahmadreza Farahani", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(30)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, "June 2021", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, "Tehran, Iran", align="C", new_x="LMARGIN", new_y="NEXT")

    # ---- TABLE OF CONTENTS ----
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 12, "Table of Contents", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)

    toc = [
        ("1", "Overview", 0),
        ("2", "Pipeline", 0),
        ("2.1", "Detection and Tracking", 1),
        ("2.2", "Lane Clustering", 1),
        ("2.3", "SVM Classification", 1),
        ("2.4", "Real-time Analysis", 1),
        ("3", "Conclusion", 0),
        ("", "References", 0),
    ]
    for num, title, indent in toc:
        pdf.set_font("Helvetica", "B" if indent == 0 else "", 11 if indent == 0 else 10)
        pdf.set_text_color(30, 30, 30)
        prefix = f"  {'    ' * indent}{num + '  ' if num else ''}"
        pdf.cell(0, 7, f"{prefix}{title}", new_x="LMARGIN", new_y="NEXT")

    # ---- SECTION 1: OVERVIEW ----
    pdf.add_page()
    pdf.chapter_title("1", "Overview")
    pdf.body_text(
        "This project was developed as part of a national initiative to measure traffic flow through "
        "monitoring cameras installed at junctions in Tehran, Iran. The system uses YOLOv4 [1] for vehicle "
        "detection, DeepSORT [2] for multi-object tracking, and a semi-supervised approach combining "
        "Spectral Clustering [3] with SVM [4] for lane classification."
    )
    pdf.body_text(
        "Note: This project uses YOLOv4 and was trained on limited data with augmentation. "
        "Many newer detection and tracking algorithms have since been developed with improved performance."
    )

    # ---- SECTION 2: PIPELINE ----
    pdf.chapter_title("2", "Pipeline")

    # 2.1 Detection and Tracking
    pdf.sub_title("2.1", "Detection and Tracking")
    pdf.body_text(
        "A custom YOLOv4 model was trained on aerial vehicle imagery. The DeepSORT algorithm [2] handles "
        "multi-object tracking using a Kalman filter [6] for state prediction and cosine distance "
        "for appearance matching."
    )
    pdf.body_text(
        "The tracker maintains vehicle identities across frames using an 8-dimensional state space:"
    )
    pdf.math_text("x = [x, y, a, h, x', y', a', h']^T")
    pdf.body_text(
        "where (x, y) is the bounding box center, a is the aspect ratio, h is the height, "
        "and the remaining components are their respective velocities."
    )
    pdf.body_text(
        "Association between detections and tracks uses a cost matrix combining appearance features "
        "(cosine distance) and motion information (Mahalanobis distance), solved via the Hungarian "
        "algorithm [5]."
    )
    pdf.add_figure(
        os.path.join(BASE, "tracking_frame.png"),
        "Figure 1: Real-time vehicle detection and tracking using YOLOv4 and DeepSORT",
    )

    # 2.2 Lane Clustering
    pdf.sub_title("2.2", "Lane Clustering")
    pdf.body_text(
        "From tracking, three features are extracted for each detected vehicle and normalized "
        "using StandardScaler:"
    )
    pdf.bullet("Horizontal position (x)")
    pdf.bullet("Vertical position (y)")
    pdf.bullet("Vehicle angle (theta)")
    pdf.body_text(
        "Spectral Clustering [3] is applied to group vehicles by lane. Processing 1000 frames yielded "
        "approximately 60,000 vehicle detections with 180,000 total features. Various clustering "
        "algorithms were evaluated using silhouette score, with Spectral Clustering producing the "
        "best results."
    )
    pdf.add_figure(
        os.path.join(BASE, "spec_4.png"),
        "Figure 2: Lane clustering using Spectral Clustering with 4 clusters",
        max_w=120,
    )

    # 2.3 SVM Classification
    pdf.sub_title("2.3", "SVM Classification")
    pdf.body_text(
        "To refine the clustering results and handle edge cases, an SVM [4] with RBF kernel was "
        "trained on the labeled data from the clustering stage:"
    )
    pdf.math_text("K(x_i, x_j) = exp(-gamma * ||x_i - x_j||^2)")
    pdf.body_text(
        "The classifier takes normalized (x, y) coordinates and predicts lane assignments, "
        "reducing errors in lane boundaries."
    )
    pdf.add_figure(
        os.path.join(BASE, "spec_4_svm.png"),
        "Figure 3: Refined lane classification after SVM training",
        max_w=120,
    )

    # 2.4 Real-time Analysis
    pdf.sub_title("2.4", "Real-time Analysis")
    pdf.body_text(
        "The final pipeline integrates all components for real-time video processing. The system "
        "classifies each detected vehicle into lanes and calculates per-lane statistics including "
        "vehicle count and average speed for traffic management applications."
    )
    pdf.add_figure(
        os.path.join(BASE, "demo_frame.png"),
        "Figure 4: Complete pipeline with lane classification and traffic analysis",
    )

    # ---- SECTION 3: CONCLUSION ----
    pdf.chapter_title("3", "Conclusion")
    pdf.body_text(
        "This project demonstrates a complete pipeline for automated traffic flow measurement from "
        "aerial imagery. The combination of deep learning-based detection (YOLOv4), robust tracking "
        "(DeepSORT with Kalman filtering), and semi-supervised lane classification (Spectral Clustering "
        "refined with SVM) provides an automated solution for traffic monitoring at scale."
    )

    # ---- REFERENCES ----
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "References", new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(60, 60, 60)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(8)

    pdf.ref_item("1",
        'A. Bochkovskiy, C.-Y. Wang, and H.-Y. M. Liao, "YOLOv4: Optimal Speed and Accuracy '
        'of Object Detection," arXiv preprint arXiv:2004.10934, 2020.'
    )
    pdf.ref_item("2",
        'N. Wojke, A. Bewley, and D. Paschke, "Simple Online and Realtime Tracking with a Deep '
        'Association Metric," in Proc. IEEE ICIP, 2017.'
    )
    pdf.ref_item("3",
        'A. Y. Ng, M. I. Jordan, and Y. Weiss, "On Spectral Clustering: Analysis and an Algorithm," '
        'in Advances in Neural Information Processing Systems (NeurIPS), vol. 14, 2001.'
    )
    pdf.ref_item("4",
        'C. Cortes and V. Vapnik, "Support-Vector Networks," Machine Learning, vol. 20, no. 3, '
        'pp. 273-297, 1995.'
    )
    pdf.ref_item("5",
        'H. W. Kuhn, "The Hungarian Method for the Assignment Problem," Naval Research Logistics '
        'Quarterly, vol. 2, no. 1-2, pp. 83-97, 1955.'
    )
    pdf.ref_item("6",
        'R. E. Kalman, "A New Approach to Linear Filtering and Prediction Problems," Journal of '
        'Basic Engineering, vol. 82, no. 1, pp. 35-45, 1960.'
    )

    out_path = os.path.join(BASE, "thesis.pdf")
    pdf.output(out_path)
    print(f"PDF generated: {out_path}")


if __name__ == "__main__":
    build_pdf()
