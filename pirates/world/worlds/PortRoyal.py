class PortRoyal:

	def __init__(self):
		scene = base.loader.loadModel('phase_4/models/islands/pir_m_are_isl_portRoyal.bam')
		#scene2 = base.loader.loadModel('phase_4/models/islands/pir_m_are_isl_portRoyal_dock_lod.bam')
		#scene3 = base.loader.loadModel('phase_4/models/islands/pir_m_are_isl_portRoyal_low.bam')
		scene4 = base.loader.loadModel('phase_4/models/islands/pir_m_are_isl_portRoyal_ocean.bam')
		scene5 = base.loader.loadModel('phase_4/models/islands/pir_m_are_isl_portRoyal_worldmap.bam')
		#scene6 = base.loader.loadModel('phase_4/models/islands/pir_m_are_isl_portRoyal_wave_idle.bam')
		scene.reparentTo(base.render)
		#scene2.reparentTo(base.render)
		#scene3.reparentTo(base.render)
		scene4.reparentTo(base.render)
		scene5.reparentTo(base.render)
		#scene6.reparentTo(base.render)

	def destroy(self):
		pass