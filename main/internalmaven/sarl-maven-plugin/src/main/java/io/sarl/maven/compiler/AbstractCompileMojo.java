/*
 * $Id$
 *
 * SARL is an general-purpose agent programming language.
 * More details on http://www.sarl.io
 *
 * Copyright (C) 2014-2018 the original authors or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package io.sarl.maven.compiler;

import java.io.File;
import java.nio.charset.Charset;
import java.text.MessageFormat;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Properties;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

import com.google.common.base.Strings;
import org.apache.maven.artifact.Artifact;
import org.apache.maven.artifact.ArtifactUtils;
import org.apache.maven.artifact.versioning.ArtifactVersion;
import org.apache.maven.artifact.versioning.DefaultArtifactVersion;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.plugins.annotations.Parameter;

import io.sarl.lang.SARLVersion;

/** Abstract Mojo for compiling SARL (standard en test).
 *
 * @author $Author: sgalland$
 * @version $FullVersion$
 * @mavengroupid $GroupId$
 * @mavenartifactid $ArtifactId$
 * @since 0.8
 */
public abstract class AbstractCompileMojo extends AbstractSarlBatchCompilerMojo {

	private static final String STUB_FOLDER = "sarl-temp"; //$NON-NLS-1$

	/** Version of the Java specification used for the source files.
	 */
	@Parameter(defaultValue = SARLVersion.MINIMAL_JDK_VERSION, required = false)
	private String source;

	/** Encoding.
	 */
	@Parameter(required = false)
	private String encoding;

	/**
	 * Location of the temporary compiler directory.
	 */
	@Parameter
	private File tempDirectory;

	/** Indicates if the Java compiler must be invoked by the SARL maven plugin.
	 */
	@Parameter(defaultValue = "true", required = false)
	private boolean runJavaCompiler;

	/** Indicates if the inline annotations must be generated by the SARL maven plugin.
	 */
	@Parameter(defaultValue = "false", required = false)
	private boolean generateInlines;

	/** Indicates if the pure annotations must be generated by the SARL maven plugin.
	 */
	@Parameter(defaultValue = "true", required = false)
	private boolean generatePures;

	/** Indicates if the trace files should be generated.
	 */
	@Parameter(defaultValue = "true", required = false)
	private boolean generateTraceFiles;

	/** Indicates if the storage files should be generated.
	 */
	@Parameter(defaultValue = "true", required = false)
	private boolean generateStorageFiles;

	/** Indicates if the equality test functions must be generated by the SARL maven plugin.
	 * @since 0.8
	 */
	@Parameter(defaultValue = "true", required = false)
	private boolean generateEqualityTestFunctions;

	/** Indicates if the toString functions must be generated by the SARL maven plugin.
	 * @since 0.8
	 */
	@Parameter(defaultValue = "true", required = false)
	private boolean generateToStringFunctions;

	/** Indicates if the clone functions must be generated by the SARL maven plugin.
	 * @since 0.8
	 */
	@Parameter(defaultValue = "true", required = false)
	private boolean generateCloneFunctions;

	/** Indicates if the serial number fields must be generated by the SARL maven plugin.
	 * @since 0.8
	 */
	@Parameter(defaultValue = "true", required = false)
	private boolean generateSerialNumberFields;

	/** Indicates if the classpath is provided by Tycho.
	 */
	@Parameter(defaultValue = "false", required = false)
	private boolean tycho;

	@Override
	protected String getSourceVersion() {
		return this.source;
	}

	@Override
	protected String getEncoding() {
		return this.encoding == null || this.encoding.isEmpty() ? Charset.defaultCharset().displayName() : this.encoding;
	}

	@Override
	protected File getTempDirectory() {
		if (this.tempDirectory == null) {
			final File targetDir = new File(getProject().getBuild().getDirectory());
			return makeAbsolute(new File(targetDir, STUB_FOLDER));
		}
		return makeAbsolute(this.tempDirectory);
	}

	@Override
	protected boolean getPostRunningOfJavaCompiler() {
		return this.runJavaCompiler;
	}

	@Override
	protected boolean getGenerateInlines() {
		return this.generateInlines;
	}

	@Override
	protected boolean getGenerateEqualityTestFunctions() {
		return this.generateEqualityTestFunctions;
	}

	@Override
	protected boolean getGenerateToStringFunctions() {
		return this.generateToStringFunctions;
	}

	@Override
	protected boolean getGenerateCloneFunctions() {
		return this.generateCloneFunctions;
	}

	@Override
	protected boolean getGenerateSerialNumberFields() {
		return this.generateSerialNumberFields;
	}

	@Override
	protected boolean getGeneratePures() {
		return this.generatePures;
	}

	@Override
	protected boolean getGenerateTraceFiles() {
		return this.generateTraceFiles;
	}

	@Override
	protected boolean getGenerateStorageFiles() {
		return this.generateStorageFiles;
	}

	@Override
	protected void buildPropertyString(StringBuilder buffer) {
		super.buildPropertyString(buffer);
		buffer.append("source = ").append(this.source).append("\n"); //$NON-NLS-1$//$NON-NLS-2$
		buffer.append("encoding = ").append(this.encoding).append("\n"); //$NON-NLS-1$//$NON-NLS-2$
		buffer.append("tempDirectory = ").append(this.tempDirectory).append("\n"); //$NON-NLS-1$//$NON-NLS-2$
		buffer.append("runJavaCompiler = ").append(this.runJavaCompiler).append("\n"); //$NON-NLS-1$//$NON-NLS-2$
		buffer.append("generateInlines = ").append(this.generateInlines).append("\n"); //$NON-NLS-1$//$NON-NLS-2$
		buffer.append("generateTraceFiles = ").append(this.generateTraceFiles).append("\n"); //$NON-NLS-1$//$NON-NLS-2$
		buffer.append("generateStorageFiles = ").append(this.generateStorageFiles).append("\n"); //$NON-NLS-1$//$NON-NLS-2$
		buffer.append("generateEqualityTestFunctions = ").append(this.generateEqualityTestFunctions).append("\n"); //$NON-NLS-1$//$NON-NLS-2$
		buffer.append("generateToStringFunctions = ").append(this.generateToStringFunctions).append("\n"); //$NON-NLS-1$//$NON-NLS-2$
		buffer.append("generateCloneFunctions = ").append(this.generateCloneFunctions).append("\n"); //$NON-NLS-1$//$NON-NLS-2$
		buffer.append("generateSerialNumberFields = ").append(this.generateSerialNumberFields).append("\n"); //$NON-NLS-1$//$NON-NLS-2$
	}

	@Override
	protected void ensureDefaultParameterValues() {
		super.ensureDefaultParameterValues();
		if (Strings.isNullOrEmpty(this.encoding)) {
			final Properties properties = this.mavenHelper.getSession().getCurrentProject().getProperties();
			this.encoding = properties.getProperty("project.build.sourceEncoding", null); //$NON-NLS-1$
			if (Strings.isNullOrEmpty(this.encoding)) {
				this.encoding = Charset.defaultCharset().name();
			}
		}
	}

	@Override
	protected void executeMojo() throws MojoExecutionException, MojoFailureException {
		ensureSARLVersions();
		validateDependencyVersions();
		compileSARL();
	}

	@SuppressWarnings("unchecked")
	private static boolean containsVersion(ArtifactVersion version, ArtifactVersion rangeMin, ArtifactVersion rangeMax) {
		return (version.compareTo(rangeMin) >= 0) && (version.compareTo(rangeMax) < 0);
	}

	private void ensureSARLVersions() throws MojoExecutionException, MojoFailureException {
		final String compilerVersionString = this.mavenHelper.getConfig("plugin.version"); //$NON-NLS-1$
		final ArtifactVersion compilerVersion = new DefaultArtifactVersion(compilerVersionString);
		final ArtifactVersion maxCompilerVersion = new DefaultArtifactVersion(
				compilerVersion.getMajorVersion() + "." //$NON-NLS-1$
				+ (compilerVersion.getMinorVersion() + 1)
				+ ".0"); //$NON-NLS-1$
		getLog().info(MessageFormat.format(Messages.CompileMojo_0, compilerVersionString, maxCompilerVersion));
		final StringBuilder classpath = new StringBuilder();
		final Set<String> foundVersions = findSARLLibrary(compilerVersion, maxCompilerVersion, classpath,
				this.tycho);
		if (foundVersions.isEmpty()) {
			throw new MojoFailureException(MessageFormat.format(Messages.CompileMojo_1, classpath.toString()));
		}
		final StringBuilder versions = new StringBuilder();
		for (final String version : foundVersions) {
			if (versions.length() > 0) {
				versions.append(", "); //$NON-NLS-1$
			}
			versions.append(version);
		}
		if (foundVersions.size() > 1) {
			getLog().info(MessageFormat.format(Messages.CompileMojo_2, versions));
		} else {
			getLog().info(MessageFormat.format(Messages.CompileMojo_3, versions));
		}
	}

	private Set<String> findSARLLibrary(ArtifactVersion compilerVersion, ArtifactVersion maxCompilerVersion,
			StringBuilder classpath, boolean enableTycho) throws MojoExecutionException, MojoFailureException {
		final String sarlLibGroupId = this.mavenHelper.getConfig("sarl-lib.groupId"); //$NON-NLS-1$
		final String sarlLibArtifactId = this.mavenHelper.getConfig("sarl-lib.artifactId"); //$NON-NLS-1$
		final String sarlLibGroupIdTycho = "p2.eclipse-plugin"; //$NON-NLS-1$
		final String sarlLibArtifactIdTycho = this.mavenHelper.getConfig("sarl-lib.osgiBundleId"); //$NON-NLS-1$
		final Set<String> foundVersions = new TreeSet<>();
		for (final Artifact dep : this.mavenHelper.getSession().getCurrentProject().getArtifacts()) {
			getLog().debug(MessageFormat.format(Messages.CompileMojo_4, dep.getGroupId(), dep.getArtifactId(), dep.getVersion()));
			if (classpath.length() > 0) {
				classpath.append(":"); //$NON-NLS-1$
			}
			classpath.append(ArtifactUtils.versionlessKey(dep));
			String gid = null;
			String aid = null;
			if (sarlLibGroupId.equals(dep.getGroupId())
					&& sarlLibArtifactId.equals(dep.getArtifactId())) {
				gid = sarlLibGroupId;
				aid = sarlLibArtifactId;
			} else if (enableTycho
					&& sarlLibGroupIdTycho.equals(dep.getGroupId())
					&& sarlLibArtifactIdTycho.equals(dep.getArtifactId())) {
				gid = sarlLibGroupIdTycho;
				aid = sarlLibArtifactIdTycho;
			}
			if (gid != null && aid != null) {
				final ArtifactVersion dependencyVersion = new DefaultArtifactVersion(dep.getVersion());
				if (!containsVersion(dependencyVersion, compilerVersion, maxCompilerVersion)) {
					final String shortMessage = MessageFormat.format(Messages.CompileMojo_5,
							gid, aid, dependencyVersion.toString(),
							compilerVersion.toString(), maxCompilerVersion.toString());
					final String longMessage = MessageFormat.format(Messages.CompileMojo_6,
							sarlLibGroupId, sarlLibArtifactId, dependencyVersion.toString(),
							compilerVersion.toString(), maxCompilerVersion.toString());
					throw new MojoFailureException(this, shortMessage, longMessage);
				}
				foundVersions.add(dep.getVersion());
			}
		}
		return foundVersions;
	}

	@SuppressWarnings("unchecked")
	private void validateDependencyVersions() throws MojoExecutionException, MojoFailureException {
		getLog().info(Messages.CompileMojo_7);
		final String sarlSdkGroupId = this.mavenHelper.getConfig("sarl-sdk.groupId"); //$NON-NLS-1$
		final String sarlSdkArtifactId = this.mavenHelper.getConfig("sarl-sdk.artifactId"); //$NON-NLS-1$

		boolean hasError = false;

		final Map<String, Artifact> artifacts = this.mavenHelper.getSession().getCurrentProject().getArtifactMap();
		final String sdkArtifactKey = ArtifactUtils.versionlessKey(sarlSdkGroupId, sarlSdkArtifactId);
		final Artifact sdkArtifact = artifacts.get(sdkArtifactKey);
		if (sdkArtifact != null) {
			final Map<String, ArtifactVersion> versions = new TreeMap<>();
			final Set<Artifact> dependencies = this.mavenHelper.resolveDependencies(sdkArtifactKey, false);
			for (final Artifact dependency : dependencies) {
				final ArtifactVersion dependencyVersion = new DefaultArtifactVersion(dependency.getVersion());
				final String dependencyKey = ArtifactUtils.versionlessKey(dependency);
				final ArtifactVersion currentVersion = versions.get(dependencyKey);
				if (currentVersion == null || dependencyVersion.compareTo(currentVersion) > 0) {
					versions.put(dependencyKey, dependencyVersion);
				}
			}

			for (final Entry<String, ArtifactVersion> entry : versions.entrySet()) {
				final Artifact dependencyArtifact = artifacts.get(entry.getKey());
				if (dependencyArtifact != null) {
					final ArtifactVersion dependencyVersion = new DefaultArtifactVersion(dependencyArtifact.getVersion());
					if (entry.getValue().compareTo(dependencyVersion) > 0) {
						final String message = MessageFormat.format(Messages.CompileMojo_8,
								dependencyArtifact.getGroupId(), dependencyArtifact.getArtifactId(),
								dependencyArtifact.getVersion(), entry.getValue().toString());
						getLog().error(message);
						hasError = true;
					}
				}
			}
		}

		if (hasError) {
			throw new MojoFailureException(Messages.CompileMojo_10);
		}
	}

	/** Run the SARL compiler.
	 *
	 * @throws MojoExecutionException if the mojo cannot be run.
	 * @throws MojoFailureException if an error occurs during the compilation.
	 */
	protected abstract void compileSARL() throws MojoExecutionException, MojoFailureException;

}
