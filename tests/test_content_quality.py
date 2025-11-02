from swoop.quality import evaluate_quality


BASELINE_HTML = """
<html><body>
<h2>Specs & Torques</h2>
<p>Tighten drain plug to 27 ft-lb (37 Nm).</p>
<p>Tighten filter housing to 18 ft-lb (24 Nm).</p>
<section id="references">
<ol>
  <li id="source-1">[1] Factory Manual</li>
  <li id="source-2">[2] Technical Bulletin</li>
</ol>
</section>
</body></html>
"""


def test_quality_report_passes_when_requirements_met():
    candidate = """
    <html><body>
    <p>Step 1<sup id="ref-1">[1]</sup></p>
    <p>Tighten drain plug to 27 ft-lb (37 Nm).</p>
    <p>Tighten filter to 18 ft-lb (24 Nm).</p>
    <section id="references">
      <ol>
        <li id="source-1">[1] Factory Manual</li>
        <li id="source-2">[2] Technical Bulletin</li>
      </ol>
    </section>
    </body></html>
    """
    report = evaluate_quality(candidate, BASELINE_HTML)
    assert report.is_pass()


def test_quality_fails_on_missing_reference():
    candidate = """
    <html><body>
    <p>Step 1<sup id="ref-1">[1]</sup></p>
    <section id="references">
      <ol>
        <li id="source-2">[2] Technical Bulletin</li>
      </ol>
    </section>
    </body></html>
    """
    report = evaluate_quality(candidate, BASELINE_HTML)
    assert 1 in report.missing_references
    assert not report.is_pass()


def test_quality_fails_when_torque_ratio_drops():
    candidate = """
    <html><body>
    <p>General service information only.</p>
    <section id="references">
      <ol>
        <li id="source-1">[1] Factory Manual</li>
        <li id="source-2">[2] Technical Bulletin</li>
      </ol>
    </section>
    </body></html>
    """
    report = evaluate_quality(candidate, BASELINE_HTML)
    assert report.torque_ratio < 0.8
    assert not report.is_pass()


def test_quality_fails_when_verify_placeholder_present():
    candidate = """
    <html><body>
    <p>Tighten drain plug <span class='verify'>Verify torque</span></p>
    <section id="references">
      <ol>
        <li id="source-1">[1] Factory Manual</li>
        <li id="source-2">[2] Technical Bulletin</li>
      </ol>
    </section>
    </body></html>
    """
    report = evaluate_quality(candidate, BASELINE_HTML)
    assert report.verify_placeholders
    assert not report.is_pass()
