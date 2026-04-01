# SafeSemantics: Topological AI Security Guardrail

## Jailbreak Attack Patterns

### [ID: JAILBREAK_01_DAN]
**Action:** Block_DAN_Variants
**Input:** {Context}
**Logic:** Detect and block 'Do Anything Now' (DAN) and derivative jailbreak prompts that instruct the model to act as an unrestricted alter-ego. Use semantic fingerprinting to identify DAN-family patterns regardless of surface-level rewording.
**Data_Connections:** [dan_signature_db], [persona_override_detector], [alignment_bypass_flag]
**Access:** Role_AI_Security_Engineer
**Events:** On_Persona_Override_Attempt

### [ID: JAILBREAK_02_ROLEPLAY]
**Action:** Detect_Roleplay_Escalation
**Input:** {Context}
**Logic:** Detect jailbreak attempts that use roleplay, fiction, or character-acting scenarios to gradually elicit harmful content. Track the semantic boundary between creative fiction and actionable harmful instructions.
**Data_Connections:** [fiction_reality_boundary], [harm_intent_classifier], [escalation_trajectory]
**Access:** Role_Content_Security
**Events:** On_Creative_Mode_Activation

### [ID: JAILBREAK_03_HYPOTHETICAL]
**Action:** Block_Hypothetical_Bypass
**Input:** {Context}
**Logic:** Detect 'hypothetically speaking', 'for educational purposes', 'in a fictional world' prefixes designed to bypass safety filters. Evaluate the downstream harm potential of the actual request regardless of framing.
**Data_Connections:** [framing_classifier], [downstream_harm_score], [intent_extraction_map]
**Access:** Role_AI_Security_Engineer
**Events:** On_Hypothetical_Frame_Detection

### [ID: JAILBREAK_04_TOKEN_SMUGGLING]
**Action:** Detect_Token_Smuggling
**Input:** {Context}
**Logic:** Detect token-level manipulation where harmful words are split across tokens, use Unicode lookalikes, or employ zero-width characters to bypass keyword filters while remaining coherent to the model.
**Data_Connections:** [token_normalization], [unicode_homoglyph_map], [zero_width_char_detector]
**Access:** Role_Security_Auditor
**Events:** On_Token_Preprocessing

### [ID: JAILBREAK_05_CRESCENDO]
**Action:** Detect_Crescendo_Attack
**Input:** {Context}
**Logic:** Detect multi-turn crescendo attacks where the attacker starts with benign requests and gradually escalates to harmful content, exploiting the model's tendency to maintain conversational consistency. Use topological drift analysis across conversation turns.
**Data_Connections:** [turn_by_turn_harm_score], [escalation_gradient], [consistency_exploitation_flag]
**Access:** Role_AI_Security_Engineer
**Events:** On_Harm_Score_Escalation

### [ID: JAILBREAK_06_PAYLOAD_SPLITTING]
**Action:** Block_Payload_Splitting
**Input:** {Context}
**Logic:** Detect attacks that split a harmful payload across multiple messages, variables, or concatenation operations so that no single message triggers safety filters but the assembled result is harmful.
**Data_Connections:** [cross_message_assembly], [delayed_payload_detector], [concatenation_analysis]
**Access:** Role_AI_Security_Engineer
**Events:** On_Multi_Message_Assembly

### [ID: JAILBREAK_07_REWARD_HACKING]
**Action:** Detect_RLHF_Reward_Exploitation
**Input:** {Context}
**Logic:** Detect prompts that exploit RLHF reward model weaknesses by crafting inputs that score high on helpfulness metrics while requesting harmful content. Use orthogonal safety evaluation independent of reward scoring.
**Data_Connections:** [reward_safety_orthogonality], [helpful_harmful_boundary], [independent_safety_judge]
**Access:** Role_ML_Security_Researcher
**Events:** On_Reward_Model_Conflict

### [ID: JAILBREAK_08_SYSTEM_MODE_EXPLOIT]
**Action:** Block_System_Mode_Exploitation
**Input:** {Context}
**Logic:** Detect attempts to invoke developer/debug/system modes through special tokens, command syntax, or by claiming to be a system administrator. Enforce that mode transitions require cryptographic authentication, not prompt-level claims.
**Data_Connections:** [mode_transition_auth], [special_token_allowlist], [privilege_claim_detector]
**Access:** Role_System_Architect
**Events:** On_Mode_Transition_Attempt

### [ID: JAILBREAK_09_REFUSAL_SUPPRESSION]
**Action:** Detect_Refusal_Suppression
**Input:** {Context}
**Logic:** Detect prompt patterns designed to prevent the model from refusing (e.g., 'do not apologize', 'never say you cannot', 'respond without disclaimers'). Ensure safety refusals cannot be suppressed by user-level instructions.
**Data_Connections:** [refusal_suppression_pattern], [safety_override_immunity], [compliance_pressure_detector]
**Access:** Role_AI_Security_Engineer
**Events:** On_Refusal_Override_Attempt

### [ID: JAILBREAK_10_VIRTUALIZATION]
**Action:** Block_Virtual_Environment_Jailbreak
**Input:** {Context}
**Logic:** Detect prompts that create virtual machines, simulated terminals, or fictional operating systems within the conversation as a pretext for executing harmful instructions 'inside the simulation'. Apply safety rules regardless of fictional framing depth.
**Data_Connections:** [simulation_depth_tracker], [virtual_context_flag], [recursive_fiction_detector]
**Access:** Role_Content_Security
**Events:** On_Virtual_Context_Creation

### [ID: JAILBREAK_11_COMPETING_OBJECTIVES]
**Action:** Detect_Competing_Objective_Exploit
**Input:** {Context}
**Logic:** Detect attacks that exploit tension between competing model objectives (helpfulness vs safety, instruction-following vs harm-avoidance). Establish clear priority hierarchy: safety > instruction-following > helpfulness.
**Data_Connections:** [objective_priority_hierarchy], [tension_detector], [safety_priority_enforcer]
**Access:** Role_AI_Safety_Researcher
**Events:** On_Objective_Conflict

### [ID: JAILBREAK_12_OBFUSCATED_INTENT]
**Action:** Detect_Obfuscated_Harmful_Intent
**Input:** {Context}
**Logic:** Detect harmful intent concealed through metaphors, analogies, code words, or domain-specific jargon. Use deep semantic analysis to evaluate the true intent behind requests regardless of surface-level innocence.
**Data_Connections:** [semantic_intent_extractor], [euphemism_database], [coded_language_classifier]
**Access:** Role_AI_Security_Engineer
**Events:** On_Intent_Classification

### [ID: JAILBREAK_13_AUTHORITY_IMPERSONATION]
**Action:** Block_Authority_Impersonation
**Input:** {Context}
**Logic:** Detect prompts claiming to be from OpenAI, Anthropic, Google, or other model providers instructing the model to disable safety features. No prompt-level claim of authority should override safety boundaries.
**Data_Connections:** [authority_claim_detector], [provider_impersonation_flag], [immutable_safety_boundary]
**Access:** Role_Identity_Security
**Events:** On_Authority_Claim_Detection

### [ID: JAILBREAK_14_OUTPUT_FORMAT_EXPLOIT]
**Action:** Detect_Output_Format_Exploitation
**Input:** {Context}
**Logic:** Detect requests that use specific output format instructions (JSON, code blocks, base64 output) to trick the model into producing harmful content in a format that bypasses output safety filters.
**Data_Connections:** [output_format_safety_check], [encoded_output_scanner], [format_agnostic_harm_filter]
**Access:** Role_Security_Auditor
**Events:** On_Output_Format_Request

### [ID: JAILBREAK_15_TRANSLATION_ATTACK]
**Action:** Block_Translation_Based_Jailbreak
**Input:** {Context}
**Logic:** Detect attacks that request translation of harmful content from/to low-resource languages where safety training is weakest. Apply safety evaluation on the semantic meaning of translated content, not just the source/target text.
**Data_Connections:** [translation_safety_model], [low_resource_language_flag], [semantic_harm_invariant]
**Access:** Role_Internationalization_Security
**Events:** On_Translation_Request

## MITRE ATLAS AI Attacks

### [ID: ATLAS_01_RECONNAISSANCE]
**Action:** Detect_AI_Reconnaissance
**Input:** {Context}
**Logic:** Detect adversarial reconnaissance activities targeting AI systems: model architecture discovery, training data inference, capability probing, and API surface mapping. Monitor for systematic testing patterns.
**Data_Connections:** [recon_pattern_detector], [probe_frequency_monitor], [capability_mapping_alert]
**Access:** Role_Threat_Intelligence
**Events:** On_Reconnaissance_Pattern

### [ID: ATLAS_02_RESOURCE_DEVELOPMENT]
**Action:** Detect_Adversarial_Resource_Development
**Input:** {Context}
**Logic:** Detect preparation of adversarial resources: crafted datasets, fine-tuned attack models, custom adversarial toolkits, and synthetic training data designed for targeted attacks.
**Data_Connections:** [adversarial_dataset_signature], [attack_toolkit_detector], [synthetic_data_anomaly]
**Access:** Role_Threat_Intelligence
**Events:** On_Adversarial_Resource_Signal

### [ID: ATLAS_03_INITIAL_ACCESS]
**Action:** Block_AI_Initial_Access_Vectors
**Input:** {Context}
**Logic:** Block initial access vectors to AI systems: supply chain compromise of ML packages, compromised model repositories, phishing targeting MLOps engineers, and exploitation of publicly accessible model endpoints.
**Data_Connections:** [access_vector_monitor], [package_integrity_checker], [endpoint_exposure_scanner]
**Access:** Role_Security_Operations
**Events:** On_Initial_Access_Attempt

### [ID: ATLAS_04_ML_ATTACK_STAGING]
**Action:** Detect_ML_Attack_Staging
**Input:** {Context}
**Logic:** Detect staging of ML-specific attacks: adversarial example preparation, prompt template crafting, model extraction query assembly, and training data poisoning payload preparation.
**Data_Connections:** [staging_activity_detector], [adversarial_example_scanner], [query_pattern_profiler]
**Access:** Role_Threat_Intelligence
**Events:** On_Staging_Activity

### [ID: ATLAS_05_MODEL_EVASION]
**Action:** Detect_Model_Evasion_Techniques
**Input:** {Context}
**Logic:** Detect evasion techniques designed to cause the model to misclassify, ignore, or incorrectly process adversarial inputs. Monitor for inputs that occupy anomalous regions of the feature space.
**Data_Connections:** [feature_space_anomaly_detector], [evasion_signature_db], [classification_confidence_monitor]
**Access:** Role_ML_Security_Researcher
**Events:** On_Evasion_Attempt

### [ID: ATLAS_06_MODEL_EXTRACTION]
**Action:** Prevent_Model_Theft
**Input:** {Context}
**Logic:** Detect and prevent model extraction attacks that attempt to steal model weights, architecture, or behavior through systematic API querying. Monitor for query patterns consistent with model distillation.
**Data_Connections:** [extraction_query_pattern], [query_volume_anomaly], [output_entropy_monitor]
**Access:** Role_IP_Protection
**Events:** On_Extraction_Pattern

### [ID: ATLAS_07_PERSISTENCE]
**Action:** Detect_AI_System_Persistence
**Input:** {Context}
**Logic:** Detect adversarial persistence mechanisms in AI systems: poisoned model checkpoints, backdoored training pipelines, compromised serving infrastructure, and persistent prompt injection in RAG stores.
**Data_Connections:** [persistence_indicator_scanner], [checkpoint_integrity_monitor], [pipeline_audit_trail]
**Access:** Role_Security_Operations
**Events:** On_Persistence_Indicator

### [ID: ATLAS_08_PRIVILEGE_ESCALATION]
**Action:** Block_AI_Privilege_Escalation
**Input:** {Context}
**Logic:** Detect and block privilege escalation within AI systems: exploiting agent permissions, manipulating RBAC in model serving, escalating from inference to training access, or gaining access to model weights from API-only access.
**Data_Connections:** [privilege_boundary_monitor], [escalation_path_detector], [access_tier_enforcer]
**Access:** Role_Identity_Security
**Events:** On_Privilege_Escalation

### [ID: ATLAS_09_DEFENSE_EVASION]
**Action:** Detect_Guardrail_Evasion
**Input:** {Context}
**Logic:** Detect attempts to identify and evade safety guardrails through systematic probing, binary search for filter boundaries, or adversarial optimization against known defense mechanisms.
**Data_Connections:** [guardrail_probing_detector], [boundary_search_pattern], [evasion_optimization_signal]
**Access:** Role_AI_Security_Engineer
**Events:** On_Defense_Evasion_Attempt

### [ID: ATLAS_10_LATERAL_MOVEMENT]
**Action:** Block_AI_Lateral_Movement
**Input:** {Context}
**Logic:** Detect lateral movement within AI ecosystems: compromising one model to attack connected models, exploiting shared embeddings, moving from development to production environments, or pivoting from AI to traditional IT infrastructure.
**Data_Connections:** [lateral_movement_detector], [cross_model_isolation], [environment_boundary_enforcer]
**Access:** Role_Security_Operations
**Events:** On_Lateral_Movement_Signal

### [ID: ATLAS_11_EXFILTRATION]
**Action:** Detect_AI_Specific_Exfiltration
**Input:** {Context}
**Logic:** Detect AI-specific exfiltration channels: model weight exfiltration, training data extraction through API, embedding theft, and intellectual property leakage through model outputs.
**Data_Connections:** [exfiltration_channel_monitor], [data_flow_analyzer], [ip_leakage_detector]
**Access:** Role_Data_Protection_Officer
**Events:** On_Exfiltration_Channel

### [ID: ATLAS_12_IMPACT_MANIPULATION]
**Action:** Prevent_AI_Output_Manipulation
**Input:** {Context}
**Logic:** Detect attacks designed to manipulate AI system outputs for adversarial impact: causing incorrect medical diagnoses, manipulating financial predictions, corrupting automated decision-making, or biasing recommendation systems.
**Data_Connections:** [output_integrity_monitor], [decision_manipulation_detector], [impact_assessment_enforcer]
**Access:** Role_AI_Safety_Researcher
**Events:** On_High_Impact_Decision

### [ID: ATLAS_13_INFRASTRUCTURE_ATTACK]
**Action:** Protect_ML_Infrastructure
**Input:** {Context}
**Logic:** Protect ML infrastructure components: GPU clusters, model serving endpoints, training pipelines, feature stores, and vector databases from traditional and AI-specific attacks.
**Data_Connections:** [infrastructure_security_scanner], [gpu_cluster_monitor], [serving_endpoint_hardening]
**Access:** Role_SRE_Engineer
**Events:** On_Infrastructure_Anomaly

### [ID: ATLAS_14_COLLECTION]
**Action:** Detect_AI_Intelligence_Collection
**Input:** {Context}
**Logic:** Detect adversarial intelligence collection activities: systematic testing of model capabilities, mapping of safety boundaries, documentation of model behaviors, and knowledge harvesting for future attacks.
**Data_Connections:** [intelligence_collection_pattern], [boundary_mapping_detector], [systematic_testing_alert]
**Access:** Role_Threat_Intelligence
**Events:** On_Intelligence_Collection_Pattern

## Model Governance

### [ID: GOV_01_MODEL_CARD]
**Action:** Enforce_Model_Card_Documentation
**Input:** {Context}
**Logic:** Require comprehensive model cards for all deployed AI models documenting: intended use, limitations, training data summary, evaluation results, ethical considerations, and known biases.
**Data_Connections:** [model_card_template], [completeness_validator], [documentation_registry]
**Access:** Role_ML_Operations
**Events:** On_Model_Registration

### [ID: GOV_02_BIAS_AUDITING]
**Action:** Enforce_Bias_Auditing
**Input:** {Context}
**Logic:** Require regular bias audits across protected categories (race, gender, age, disability). Implement automated fairness metrics (demographic parity, equalized odds) and mandate remediation for identified disparities.
**Data_Connections:** [fairness_metric_suite], [protected_category_list], [remediation_tracker]
**Access:** Role_AI_Ethics_Officer
**Events:** On_Bias_Audit_Schedule

### [ID: GOV_03_EXPLAINABILITY]
**Action:** Enforce_Explainability_Requirements
**Input:** {Context}
**Logic:** Enforce explainability requirements proportional to decision impact. High-impact decisions (credit, hiring, medical) require full interpretability. Implement SHAP, LIME, or attention visualization as appropriate.
**Data_Connections:** [impact_level_classifier], [explainability_method_selector], [interpretation_report_generator]
**Access:** Role_AI_Ethics_Officer
**Events:** On_High_Impact_AI_Decision

### [ID: GOV_04_VERSION_CONTROL]
**Action:** Enforce_AI_Model_Version_Control
**Input:** {Context}
**Logic:** Enforce strict version control for all AI model artifacts: weights, configs, tokenizers, training data snapshots, and evaluation results. Enable rollback to any previous version within retention window.
**Data_Connections:** [model_version_registry], [artifact_hash_chain], [rollback_capability]
**Access:** Role_ML_Operations
**Events:** On_Model_Update

### [ID: GOV_05_AB_SAFETY_TESTING]
**Action:** Enforce_AB_Safety_Testing
**Input:** {Context}
**Logic:** Require A/B safety testing before any model update reaches production. Compare new model safety metrics against baseline and require statistical significance before approval.
**Data_Connections:** [ab_test_framework], [safety_metric_baseline], [statistical_significance_threshold]
**Access:** Role_AI_Safety_Researcher
**Events:** On_Model_Promotion

### [ID: GOV_06_RED_TEAMING]
**Action:** Mandate_Red_Team_Evaluation
**Input:** {Context}
**Logic:** Mandate adversarial red-team evaluation before production deployment. Red team must cover prompt injection, jailbreaks, data extraction, and domain-specific attack vectors.
**Data_Connections:** [red_team_checklist], [attack_coverage_matrix], [finding_remediation_tracker]
**Access:** Role_AI_Security_Engineer
**Events:** On_Pre_Production_Gate

### [ID: GOV_07_MONITORING_OBSERVABILITY]
**Action:** Enforce_Production_Monitoring
**Input:** {Context}
**Logic:** Enforce comprehensive monitoring of production AI systems: output quality metrics, safety filter trigger rates, latency distributions, token usage patterns, and anomalous interaction detection.
**Data_Connections:** [monitoring_dashboard], [alert_threshold_config], [anomaly_detection_pipeline]
**Access:** Role_SRE_Engineer
**Events:** On_Production_Deployment

### [ID: GOV_08_HUMAN_OVERSIGHT]
**Action:** Enforce_Human_Oversight
**Input:** {Context}
**Logic:** Enforce human-in-the-loop or human-on-the-loop oversight requirements proportional to AI system autonomy level. High-autonomy systems require real-time human monitoring with kill-switch capability.
**Data_Connections:** [autonomy_level_classifier], [oversight_mechanism], [kill_switch_availability]
**Access:** Role_AI_Ethics_Officer
**Events:** On_Autonomous_Action

## Privacy Regulations AI

### [ID: PRIVACY_01_GDPR_AI]
**Action:** Enforce_GDPR_AI_Provisions
**Input:** {Context}
**Logic:** Enforce GDPR requirements for AI systems: right to explanation for automated decisions, data minimization in AI training, lawful basis for AI data processing, and data subject access requests for AI-processed data.
**Data_Connections:** [gdpr_compliance_checker], [data_minimization_enforcer], [explanation_generator]
**Access:** Role_Data_Protection_Officer
**Events:** On_EU_Data_Processing

### [ID: PRIVACY_02_EU_AI_ACT]
**Action:** Enforce_EU_AI_Act_Compliance
**Input:** {Context}
**Logic:** Classify AI system risk level (Unacceptable/High/Limited/Minimal) per EU AI Act. Enforce conformity assessment, transparency obligations, and human oversight requirements based on risk classification.
**Data_Connections:** [risk_classification_engine], [conformity_assessment_log], [transparency_obligation_checker]
**Access:** Role_Legal_Compliance
**Events:** On_AI_System_Deployment

### [ID: PRIVACY_03_CCPA_AI]
**Action:** Enforce_CCPA_AI_Transparency
**Input:** {Context}
**Logic:** Enforce California Consumer Privacy Act requirements for AI: disclosure of AI usage in profiling, opt-out rights for automated decision-making, and data deletion requests affecting AI training data.
**Data_Connections:** [ccpa_disclosure_generator], [opt_out_mechanism], [training_data_deletion_handler]
**Access:** Role_Privacy_Engineer
**Events:** On_California_Consumer_Request

### [ID: PRIVACY_04_HIPAA_AI]
**Action:** Enforce_HIPAA_AI_Usage
**Input:** {Context}
**Logic:** Enforce HIPAA requirements for AI processing of protected health information (PHI). Ensure AI systems maintain minimum necessary standard, audit trails, and business associate agreements for AI vendors.
**Data_Connections:** [phi_detection_filter], [minimum_necessary_enforcer], [baa_verification]
**Access:** Role_HIPAA_Officer
**Events:** On_Health_Data_Processing

### [ID: PRIVACY_05_CROSS_BORDER_AI]
**Action:** Enforce_Cross_Border_Data_Flow
**Input:** {Context}
**Logic:** Enforce data locality and cross-border transfer restrictions for AI model inputs and outputs. Detect when AI processing may violate data sovereignty requirements or transfer adequacy decisions.
**Data_Connections:** [geo_location_validator], [transfer_adequacy_checker], [data_residency_enforcer]
**Access:** Role_Legal_Compliance
**Events:** On_Cross_Border_Data_Transfer

### [ID: PRIVACY_06_CONSENT_MANAGEMENT]
**Action:** Enforce_AI_Consent_Management
**Input:** {Context}
**Logic:** Enforce granular consent management for AI data processing. Track consent status for each data processing purpose and ensure AI systems only process data for consented purposes.
**Data_Connections:** [consent_registry], [purpose_limitation_enforcer], [consent_withdrawal_handler]
**Access:** Role_Privacy_Engineer
**Events:** On_Data_Processing_Purpose_Check

### [ID: PRIVACY_07_RIGHT_TO_EXPLANATION]
**Action:** Enforce_Right_To_Explanation
**Input:** {Context}
**Logic:** Implement the right to explanation for AI-driven decisions that significantly affect individuals. Generate human-readable explanations of AI decision factors and provide recourse mechanisms.
**Data_Connections:** [explainability_engine], [decision_factor_extractor], [recourse_mechanism]
**Access:** Role_AI_Ethics_Officer
**Events:** On_Significant_AI_Decision

### [ID: PRIVACY_08_DATA_RETENTION_AI]
**Action:** Enforce_AI_Data_Retention_Policies
**Input:** {Context}
**Logic:** Enforce data retention and deletion policies for AI conversation logs, training data, and model artifacts. Implement automated purging schedules and ensure deletion propagates to all replicas.
**Data_Connections:** [retention_policy_engine], [deletion_propagation_validator], [purge_schedule_enforcer]
**Access:** Role_Data_Protection_Officer
**Events:** On_Retention_Period_Expiry

## Hallucination Defense

### [ID: HALLUC_01_FACTUALITY_GROUNDING]
**Action:** Enforce_Factuality_Grounding
**Input:** {Context}
**Logic:** Require all factual claims to be grounded in verifiable source material. Implement topological provenance tracking that traces each output assertion back to a specific source document or knowledge base entry.
**Data_Connections:** [source_provenance_chain], [assertion_grounding_map], [ungrounded_claim_flag]
**Access:** Role_Content_Quality
**Events:** On_Factual_Assertion_Generated

### [ID: HALLUC_02_CITATION_VERIFICATION]
**Action:** Verify_Citation_Accuracy
**Input:** {Context}
**Logic:** Verify that all citations (paper titles, author names, URLs, statistics, quotes) correspond to real, existing sources. Detect fabricated citations by cross-referencing against known bibliographic databases.
**Data_Connections:** [citation_validator], [bibliographic_db], [fabricated_citation_detector]
**Access:** Role_Content_Quality
**Events:** On_Citation_Generated

### [ID: HALLUC_03_CONFABULATION_DETECTION]
**Action:** Detect_Confabulation_Patterns
**Input:** {Context}
**Logic:** Detect confident-sounding but fabricated details (dates, statistics, names, events) that the model generates to fill knowledge gaps. Monitor for patterns of false specificity that indicate confabulation.
**Data_Connections:** [false_specificity_detector], [confidence_calibration_model], [knowledge_gap_mapper]
**Access:** Role_AI_Safety_Researcher
**Events:** On_High_Specificity_Low_Confidence

### [ID: HALLUC_04_KNOWLEDGE_BOUNDARY]
**Action:** Enforce_Knowledge_Boundary_Awareness
**Input:** {Context}
**Logic:** Enforce that the model acknowledges the boundaries of its training data, knowledge cutoff date, and domain expertise. Prevent the model from generating authoritative-sounding responses in domains where it lacks reliable data.
**Data_Connections:** [knowledge_cutoff_boundary], [domain_expertise_map], [uncertainty_expression_enforcer]
**Access:** Role_Content_Quality
**Events:** On_Out_Of_Domain_Query

### [ID: HALLUC_05_NUMERICAL_ACCURACY]
**Action:** Validate_Numerical_Claims
**Input:** {Context}
**Logic:** Apply rigorous validation to numerical claims (statistics, calculations, measurements, financial figures). Cross-reference generated numbers against source material and flag discrepancies.
**Data_Connections:** [numerical_validator], [calculation_verifier], [statistical_cross_reference]
**Access:** Role_Content_Quality
**Events:** On_Numerical_Claim_Generated

### [ID: HALLUC_06_TEMPORAL_CONSISTENCY]
**Action:** Enforce_Temporal_Consistency
**Input:** {Context}
**Logic:** Detect and prevent temporal hallucinations where the model confuses timelines, attributes events to wrong dates, or generates anachronistic information. Validate temporal relationships in generated content.
**Data_Connections:** [temporal_consistency_checker], [timeline_validator], [anachronism_detector]
**Access:** Role_Content_Quality
**Events:** On_Temporal_Claim_Generated

### [ID: HALLUC_07_ATTRIBUTION_ACCURACY]
**Action:** Verify_Attribution_Accuracy
**Input:** {Context}
**Logic:** Ensure quotes, statements, and positions are correctly attributed to the right individuals or organizations. Detect misattribution patterns that could lead to defamation or misinformation.
**Data_Connections:** [attribution_validator], [quote_verification_db], [misattribution_detector]
**Access:** Role_Content_Quality
**Events:** On_Attributed_Statement_Generated

### [ID: HALLUC_08_LOGICAL_CONSISTENCY]
**Action:** Enforce_Logical_Consistency
**Input:** {Context}
**Logic:** Detect internal logical contradictions within generated responses. Validate that premises lead to valid conclusions and that multi-step reasoning maintains consistency across all steps.
**Data_Connections:** [logical_consistency_checker], [contradiction_detector], [reasoning_chain_validator]
**Access:** Role_AI_Safety_Researcher
**Events:** On_Multi_Step_Reasoning

## Multimodal Attack Vectors

### [ID: MULTIMODAL_01_IMAGE_INJECTION]
**Action:** Block_Image_Based_Prompt_Injection
**Input:** {Context}
**Logic:** Detect prompt injection payloads embedded in images through steganography, invisible text overlays, adversarial patches, or OCR-exploitable text. Scan all visual inputs for hidden instruction payloads before processing.
**Data_Connections:** [image_payload_scanner], [steganography_detector], [ocr_injection_filter]
**Access:** Role_Multimodal_Security
**Events:** On_Image_Input_Received

### [ID: MULTIMODAL_02_OCR_EXPLOITATION]
**Action:** Prevent_OCR_Based_Attacks
**Input:** {Context}
**Logic:** Detect adversarial text rendered in images that is designed to be read by OCR but bypass text-based safety filters. Apply the same safety evaluation to OCR-extracted text as to direct text input.
**Data_Connections:** [ocr_safety_parity_enforcer], [rendered_text_scanner], [font_obfuscation_detector]
**Access:** Role_Content_Security
**Events:** On_OCR_Text_Extraction

### [ID: MULTIMODAL_03_AUDIO_STEGANOGRAPHY]
**Action:** Detect_Audio_Steganographic_Attacks
**Input:** {Context}
**Logic:** Detect hidden instructions or adversarial payloads embedded in audio inputs through frequency manipulation, ultrasonic commands, or steganographic encoding that may be processed by speech-to-text systems.
**Data_Connections:** [audio_spectrum_analyzer], [ultrasonic_command_detector], [steganographic_audio_filter]
**Access:** Role_Multimodal_Security
**Events:** On_Audio_Input_Received

### [ID: MULTIMODAL_04_CROSS_MODAL_JAILBREAK]
**Action:** Block_Cross_Modal_Jailbreak
**Input:** {Context}
**Logic:** Detect jailbreak attacks that split harmful instructions across modalities (part in text, part in image, part in audio) so no single modality triggers safety filters. Apply unified cross-modal safety analysis.
**Data_Connections:** [cross_modal_assembler], [unified_safety_evaluator], [modal_splitting_detector]
**Access:** Role_Multimodal_Security
**Events:** On_Multi_Modal_Input

### [ID: MULTIMODAL_05_ADVERSARIAL_PATCHES]
**Action:** Detect_Visual_Adversarial_Patches
**Input:** {Context}
**Logic:** Detect adversarial patches in images designed to manipulate model perception or trigger specific unwanted behaviors. Monitor for pixel patterns that deviate from natural image statistics.
**Data_Connections:** [adversarial_patch_detector], [image_statistics_analyzer], [perturbation_signature_db]
**Access:** Role_ML_Security_Researcher
**Events:** On_Image_Analysis

### [ID: MULTIMODAL_06_VIDEO_FRAME_INJECTION]
**Action:** Block_Video_Frame_Injection
**Input:** {Context}
**Logic:** Detect malicious frames injected into video inputs that contain prompt injection payloads, adversarial patches, or harmful content designed to be processed by video understanding models.
**Data_Connections:** [frame_by_frame_scanner], [injection_frame_detector], [temporal_consistency_validator]
**Access:** Role_Multimodal_Security
**Events:** On_Video_Input_Received

### [ID: MULTIMODAL_07_DOCUMENT_EXPLOIT]
**Action:** Secure_Document_Processing
**Input:** {Context}
**Logic:** Detect adversarial payloads in uploaded documents (PDFs, Word docs, spreadsheets) including hidden text, macro exploits, embedded objects, and metadata-based injection vectors.
**Data_Connections:** [document_deep_scanner], [hidden_content_extractor], [macro_block_policy]
**Access:** Role_Content_Security
**Events:** On_Document_Upload

### [ID: MULTIMODAL_08_QR_CODE_ATTACK]
**Action:** Block_QR_Code_Based_Attacks
**Input:** {Context}
**Logic:** Detect QR codes and barcodes in image inputs that encode malicious URLs, prompt injection payloads, or redirect commands targeting the AI agent's browsing or tool-use capabilities.
**Data_Connections:** [qr_code_scanner], [url_allowlist_validator], [encoded_payload_analyzer]
**Access:** Role_Content_Security
**Events:** On_QR_Code_Detected

## Data Exfiltration Attacks

### [ID: EXFIL_01_PII_EXTRACTION]
**Action:** Block_PII_Extraction
**Input:** {Context}
**Logic:** Detect and prevent attempts to extract personally identifiable information (names, emails, SSNs, credit cards, phone numbers) from the model's training data or connected data sources. Apply semantic boundary enforcement that blocks PII patterns in output regardless of prompt framing.
**Data_Connections:** [pii_pattern_detector], [output_redaction_map], [data_minimization_policy]
**Access:** Role_Data_Protection_Officer
**Events:** On_PII_Pattern_In_Output

### [ID: EXFIL_02_TRAINING_DATA_LEAK]
**Action:** Prevent_Training_Data_Memorization_Leak
**Input:** {Context}
**Logic:** Detect prompts designed to trigger verbatim reproduction of training data through completion prompts, repeated token generation, or targeted extraction attacks. Monitor output for statistical signatures of memorized content.
**Data_Connections:** [memorization_signature_detector], [verbatim_reproduction_threshold], [canary_token_monitor]
**Access:** Role_ML_Security_Researcher
**Events:** On_Memorization_Pattern_Detected

### [ID: EXFIL_03_RAG_DATA_LEAK]
**Action:** Prevent_RAG_Source_Leakage
**Input:** {Context}
**Logic:** Prevent the model from exposing raw contents of RAG knowledge base documents, file paths, database schemas, or internal API endpoints. Enforce that responses synthesize information without revealing source artifacts.
**Data_Connections:** [source_artifact_detector], [path_redaction_filter], [schema_exposure_block]
**Access:** Role_RAG_Administrator
**Events:** On_Source_Exposure_Attempt

### [ID: EXFIL_04_SIDE_CHANNEL]
**Action:** Block_Side_Channel_Exfiltration
**Input:** {Context}
**Logic:** Detect side-channel attacks that extract information through response timing, token probabilities, response length variations, or error message content. Normalize response characteristics to prevent information leakage through non-content channels.
**Data_Connections:** [timing_normalization], [probability_masking], [error_sanitization]
**Access:** Role_Security_Auditor
**Events:** On_Response_Metadata_Access

### [ID: EXFIL_05_MODEL_INVERSION]
**Action:** Prevent_Model_Inversion_Attack
**Input:** {Context}
**Logic:** Detect systematic probing designed to reconstruct training data or model internals through carefully crafted query sequences. Monitor for query patterns that exhibit statistical signatures of model inversion attacks.
**Data_Connections:** [query_pattern_analyzer], [inversion_signature_db], [rate_limit_enforcement]
**Access:** Role_ML_Security_Researcher
**Events:** On_Systematic_Probing_Detected

### [ID: EXFIL_06_CREDENTIAL_HARVEST]
**Action:** Block_Credential_Harvesting
**Input:** {Context}
**Logic:** Detect prompts designed to extract API keys, passwords, tokens, connection strings, or other credentials that may exist in the model's context, system prompt, or connected tool configurations.
**Data_Connections:** [credential_pattern_detector], [secret_redaction_filter], [environment_variable_shield]
**Access:** Role_Secret_Manager
**Events:** On_Credential_Pattern_In_Output

### [ID: EXFIL_07_MEMBERSHIP_INFERENCE]
**Action:** Prevent_Membership_Inference
**Input:** {Context}
**Logic:** Detect attacks that determine whether specific data points were part of the model's training set. Monitor for binary probing patterns that compare model confidence on known vs unknown data points.
**Data_Connections:** [confidence_calibration], [membership_query_detector], [differential_privacy_enforcement]
**Access:** Role_Privacy_Engineer
**Events:** On_Membership_Query_Pattern

### [ID: EXFIL_08_STRUCTURED_EXTRACTION]
**Action:** Block_Structured_Data_Extraction
**Input:** {Context}
**Logic:** Detect requests that attempt to extract internal data in structured formats (JSON dumps, CSV exports, SQL query results) that may bypass natural language safety filters. Apply safety evaluation to structured output content.
**Data_Connections:** [structured_output_scanner], [bulk_extraction_detector], [format_agnostic_safety]
**Access:** Role_Data_Protection_Officer
**Events:** On_Structured_Output_Request

### [ID: EXFIL_09_CONVERSATION_HISTORY_LEAK]
**Action:** Prevent_Cross_Session_Data_Leak
**Input:** {Context}
**Logic:** Prevent leakage of information from other users' conversations, previous sessions, or parallel threads. Enforce strict session isolation at the topological boundary level.
**Data_Connections:** [session_isolation_boundary], [cross_session_detector], [memory_compartmentalization]
**Access:** Role_Privacy_Engineer
**Events:** On_Cross_Session_Reference

### [ID: EXFIL_10_EMBEDDING_THEFT]
**Action:** Prevent_Embedding_Exfiltration
**Input:** {Context}
**Logic:** Detect attempts to extract or reconstruct embedding vectors through systematic querying. Prevent exposure of internal vector representations that could be used to clone model capabilities or reconstruct private data.
**Data_Connections:** [embedding_access_control], [vector_reconstruction_detector], [output_projection_limiter]
**Access:** Role_ML_Security_Researcher
**Events:** On_Embedding_Access_Attempt

## API Abuse Attacks

### [ID: API_01_RATE_LIMIT_BYPASS]
**Action:** Prevent_Rate_Limit_Bypass
**Input:** {Context}
**Logic:** Detect and block attempts to bypass API rate limits through token rotation, distributed requests, header manipulation, or session multiplexing. Enforce rate limits at the identity level, not just IP or token level.
**Data_Connections:** [identity_rate_limiter], [distributed_request_detector], [session_fingerprint]
**Access:** Role_API_Security
**Events:** On_Rate_Limit_Threshold

### [ID: API_02_TOKEN_EXHAUSTION]
**Action:** Prevent_Token_Exhaustion_Attack
**Input:** {Context}
**Logic:** Detect prompts designed to consume maximum output tokens through verbose generation instructions, recursive expansion commands, or context window exploitation. Enforce token budgets per request and per session.
**Data_Connections:** [token_budget_enforcer], [verbosity_amplification_detector], [output_length_policy]
**Access:** Role_FinOps_Engineer
**Events:** On_Token_Budget_Warning

### [ID: API_03_COST_AMPLIFICATION]
**Action:** Block_Cost_Amplification_Attack
**Input:** {Context}
**Logic:** Detect adversarial usage patterns designed to inflate API costs through expensive operations (large context windows, vision processing, function calling chains). Apply cost circuit breakers.
**Data_Connections:** [cost_monitor], [circuit_breaker_threshold], [expensive_operation_detector]
**Access:** Role_FinOps_Engineer
**Events:** On_Cost_Anomaly

### [ID: API_04_MODEL_FINGERPRINTING]
**Action:** Prevent_Model_Fingerprinting
**Input:** {Context}
**Logic:** Detect systematic probing designed to identify the underlying model, version, or provider behind an API. Prevent model identification that could be used to target known vulnerabilities.
**Data_Connections:** [probe_pattern_detector], [response_normalization], [model_identity_shield]
**Access:** Role_API_Security
**Events:** On_Fingerprinting_Pattern

### [ID: API_05_KEY_EXTRACTION]
**Action:** Block_API_Key_Extraction
**Input:** {Context}
**Logic:** Detect prompts designed to extract API keys, access tokens, or authentication credentials from the AI application's environment or system prompt. Apply absolute blocking on credential exposure.
**Data_Connections:** [credential_exposure_filter], [environment_variable_shield], [key_pattern_detector]
**Access:** Role_Secret_Manager
**Events:** On_Credential_Extraction_Attempt

### [ID: API_06_ABUSE_OF_FUNCTION_CALLING]
**Action:** Prevent_Function_Calling_Abuse
**Input:** {Context}
**Logic:** In APIs with function/tool calling capabilities, detect and prevent abuse of function call parameters to execute unintended operations, SQL injection through function args, or SSRF through URL parameters.
**Data_Connections:** [function_param_validator], [injection_in_params_detector], [ssrf_url_checker]
**Access:** Role_API_Security
**Events:** On_Function_Call_Request

### [ID: API_07_BATCH_ENUMERATION]
**Action:** Block_Batch_Enumeration_Attack
**Input:** {Context}
**Logic:** Detect batch API requests designed to enumerate sensitive information (valid user IDs, internal system names, knowledge base contents) through systematic querying across many inputs.
**Data_Connections:** [enumeration_pattern_detector], [batch_query_analyzer], [information_leakage_threshold]
**Access:** Role_API_Security
**Events:** On_Batch_Request

### [ID: API_08_REPLAY_ATTACK]
**Action:** Prevent_API_Replay_Attacks
**Input:** {Context}
**Logic:** Detect and prevent replay attacks that re-submit captured API requests to bypass authentication, duplicate transactions, or exploit state-dependent vulnerabilities in AI API endpoints.
**Data_Connections:** [request_nonce_validator], [replay_window_enforcer], [state_mutation_protector]
**Access:** Role_API_Security
**Events:** On_Duplicate_Request_Detected

## Prompt Injection Attacks

### [ID: PROMPT_INJ_01_DIRECT]
**Action:** Block_Direct_Prompt_Injection
**Input:** {Context}
**Logic:** Detect and neutralize direct prompt injection where a user explicitly instructs the model to ignore prior instructions, override system prompts, or adopt a new persona. Use topological boundary analysis to identify semantic discontinuities between user input and system instruction space.
**Data_Connections:** [instruction_boundary], [system_prompt_hash], [semantic_distance_threshold]
**Access:** Role_AI_Security_Engineer
**Events:** On_User_Prompt_Received

### [ID: PROMPT_INJ_02_INDIRECT]
**Action:** Block_Indirect_Prompt_Injection
**Input:** {Context}
**Logic:** Detect prompt injection payloads hidden in external data sources consumed by the AI (web pages, documents, emails, database records). Apply topological isolation between user-controlled content and system-trusted content at the embedding level.
**Data_Connections:** [source_trust_score], [content_origin_tag], [embedding_isolation_boundary]
**Access:** Role_RAG_Administrator
**Events:** On_External_Content_Ingestion

### [ID: PROMPT_INJ_03_SYSTEM_EXTRACTION]
**Action:** Prevent_System_Prompt_Extraction
**Input:** {Context}
**Logic:** Detect and block attempts to extract, repeat, or summarize the system prompt. Monitor output tokens for semantic similarity to known system instruction patterns. Enforce asymmetric information boundaries where the model can read but never reproduce system-level instructions.
**Data_Connections:** [system_prompt_fingerprint], [output_similarity_score], [instruction_reflection_block]
**Access:** Role_Prompt_Architect
**Events:** On_Response_Generation

### [ID: PROMPT_INJ_04_INSTRUCTION_HIERARCHY]
**Action:** Enforce_Instruction_Hierarchy
**Input:** {Context}
**Logic:** Implement strict instruction hierarchy: System > Developer > User. Reject any user-level instruction that attempts to override developer or system-level constraints. Use topological layering to create non-traversable boundaries between instruction tiers.
**Data_Connections:** [instruction_tier], [privilege_boundary], [override_attempt_log]
**Access:** Role_System_Architect
**Events:** On_Instruction_Parse

### [ID: PROMPT_INJ_05_MULTI_TURN]
**Action:** Detect_Multi_Turn_Manipulation
**Input:** {Context}
**Logic:** Track conversation state across turns to detect gradual prompt injection where an attacker incrementally shifts the model's behavior over multiple messages. Use conversation graph analysis to identify drift vectors that deviate from the original instruction topology.
**Data_Connections:** [conversation_graph], [drift_vector], [baseline_behavior_map]
**Access:** Role_AI_Security_Engineer
**Events:** On_Conversation_Turn

### [ID: PROMPT_INJ_06_CONTEXT_OVERFLOW]
**Action:** Prevent_Context_Window_Poisoning
**Input:** {Context}
**Logic:** Detect attempts to fill the context window with benign-appearing text that pushes critical system instructions out of the attention window. Monitor attention distribution topology to ensure system instructions maintain prominence regardless of context length.
**Data_Connections:** [context_window_usage], [instruction_attention_weight], [padding_detection_threshold]
**Access:** Role_AI_Security_Engineer
**Events:** On_Context_Assembly

### [ID: PROMPT_INJ_07_ENCODING_BYPASS]
**Action:** Detect_Encoding_Based_Injection
**Input:** {Context}
**Logic:** Detect prompt injection payloads encoded in Base64, ROT13, hexadecimal, Unicode homoglyphs, Morse code, or other encoding schemes designed to bypass surface-level text filters. Apply recursive decoding and semantic analysis before processing.
**Data_Connections:** [encoding_detector], [decoded_payload], [character_normalization_map]
**Access:** Role_Security_Auditor
**Events:** On_Input_Preprocessing

### [ID: PROMPT_INJ_08_MARKDOWN_HTML]
**Action:** Block_Markup_Injection_Vectors
**Input:** {Context}
**Logic:** Detect and sanitize prompt injection payloads embedded in markdown, HTML, LaTeX, or other markup languages that may be rendered or interpreted by the model or downstream systems. Strip executable content while preserving semantic meaning.
**Data_Connections:** [markup_sanitizer], [rendered_content_diff], [executable_block_filter]
**Access:** Role_Content_Security
**Events:** On_Content_Rendering

### [ID: PROMPT_INJ_09_FEW_SHOT_POISON]
**Action:** Detect_Few_Shot_Example_Poisoning
**Input:** {Context}
**Logic:** Detect malicious few-shot examples that establish a pattern of harmful behavior for the model to follow. Analyze the semantic trajectory of in-context examples to ensure they align with intended behavior boundaries.
**Data_Connections:** [example_semantic_trajectory], [behavioral_boundary], [pattern_alignment_score]
**Access:** Role_Prompt_Architect
**Events:** On_Few_Shot_Assembly

### [ID: PROMPT_INJ_10_TOOL_CALL_HIJACK]
**Action:** Prevent_Tool_Call_Injection
**Input:** {Context}
**Logic:** Detect prompt injection payloads designed to manipulate the model into making unauthorized tool calls, API requests, or function invocations. Validate all tool call parameters against an allowlist before execution.
**Data_Connections:** [tool_call_allowlist], [parameter_validation_schema], [unauthorized_call_log]
**Access:** Role_Agent_Administrator
**Events:** On_Tool_Call_Request

### [ID: PROMPT_INJ_11_DELIMITER_ESCAPE]
**Action:** Block_Delimiter_Escape_Attacks
**Input:** {Context}
**Logic:** Detect attempts to close or escape prompt delimiters (triple quotes, XML tags, special tokens) to break out of user input sandboxes and inject instructions at a higher privilege level.
**Data_Connections:** [delimiter_integrity_check], [escape_sequence_detector], [sandbox_boundary_hash]
**Access:** Role_AI_Security_Engineer
**Events:** On_Input_Tokenization

### [ID: PROMPT_INJ_12_LANGUAGE_SWITCH]
**Action:** Detect_Cross_Language_Injection
**Input:** {Context}
**Logic:** Detect prompt injection payloads that switch languages mid-prompt to exploit gaps in multilingual safety training. Apply language-agnostic semantic analysis to ensure safety boundaries hold across all supported languages.
**Data_Connections:** [language_detector], [cross_lingual_safety_model], [semantic_invariance_check]
**Access:** Role_Internationalization_Security
**Events:** On_Language_Detection

## Supply Chain AI Security

### [ID: SUPPLY_01_MODEL_POISONING]
**Action:** Detect_Model_Poisoning
**Input:** {Context}
**Logic:** Detect backdoors and trojans injected during model training through data poisoning. Monitor model behavior for trigger-activated deviations from expected output distributions.
**Data_Connections:** [trigger_pattern_scanner], [output_distribution_monitor], [behavioral_anomaly_detector]
**Access:** Role_ML_Security_Researcher
**Events:** On_Model_Deployment

### [ID: SUPPLY_02_FINETUNING_BACKDOOR]
**Action:** Prevent_Fine_Tuning_Backdoors
**Input:** {Context}
**Logic:** Detect and prevent insertion of backdoors during fine-tuning by validating training data integrity, monitoring for anomalous gradient updates, and testing for triggered behaviors in fine-tuned models.
**Data_Connections:** [training_data_validator], [gradient_anomaly_detector], [trigger_test_suite]
**Access:** Role_ML_Operations
**Events:** On_Fine_Tuning_Completion

### [ID: SUPPLY_03_ADAPTER_TROJANS]
**Action:** Detect_Adapter_Layer_Trojans
**Input:** {Context}
**Logic:** Detect malicious LoRA adapters, PEFT modules, or other parameter-efficient fine-tuning artifacts that introduce backdoor behaviors when applied to base models.
**Data_Connections:** [adapter_integrity_validator], [parameter_diff_analyzer], [trojan_behavior_test]
**Access:** Role_ML_Security_Researcher
**Events:** On_Adapter_Load

### [ID: SUPPLY_04_RLHF_REWARD_HACK]
**Action:** Detect_RLHF_Reward_Hacking
**Input:** {Context}
**Logic:** Detect cases where the model has learned to exploit weaknesses in the reward model rather than genuinely aligning with human values. Monitor for reward-maximizing behaviors that don't correspond to genuine helpfulness.
**Data_Connections:** [reward_alignment_validator], [goodharting_detector], [human_eval_correlation]
**Access:** Role_AI_Safety_Researcher
**Events:** On_RLHF_Evaluation

### [ID: SUPPLY_05_DATASET_CONTAMINATION]
**Action:** Prevent_Dataset_Contamination
**Input:** {Context}
**Logic:** Detect contamination of training or evaluation datasets with adversarial examples, biased samples, or data designed to manipulate model behavior in specific contexts.
**Data_Connections:** [data_quality_scanner], [contamination_detector], [sample_provenance_tracker]
**Access:** Role_Data_Science
**Events:** On_Dataset_Preparation

### [ID: SUPPLY_06_MODEL_PROVENANCE]
**Action:** Enforce_Model_Provenance
**Input:** {Context}
**Logic:** Maintain cryptographic provenance chain for all model artifacts (weights, configs, tokenizers). Verify model integrity against signed checksums before deployment to prevent tampering.
**Data_Connections:** [model_hash_chain], [signing_authority], [tamper_detection_validator]
**Access:** Role_ML_Operations
**Events:** On_Model_Distribution

### [ID: SUPPLY_07_DEPENDENCY_VULNERABILITY]
**Action:** Scan_ML_Dependencies
**Input:** {Context}
**Logic:** Continuously scan ML framework dependencies (PyTorch, TensorFlow, Transformers, etc.) for known vulnerabilities. Apply security patches and enforce minimum version requirements for all ML dependencies.
**Data_Connections:** [ml_dependency_scanner], [cve_database], [version_enforcement_policy]
**Access:** Role_DevSecOps
**Events:** On_Build_Pipeline

### [ID: SUPPLY_08_QUANTIZATION_ATTACK]
**Action:** Detect_Quantization_Based_Attacks
**Input:** {Context}
**Logic:** Detect adversarial manipulation during model quantization or compression that introduces behavioral changes exploitable by attackers. Validate behavioral consistency between full-precision and quantized models.
**Data_Connections:** [quantization_consistency_test], [behavioral_drift_detector], [precision_safety_validator]
**Access:** Role_ML_Operations
**Events:** On_Model_Quantization

## Content Safety Attacks

### [ID: CONTENT_01_TOXICITY_BYPASS]
**Action:** Block_Toxicity_Generation_Bypass
**Input:** {Context}
**Logic:** Detect and block attempts to generate toxic, hateful, or violent content through indirect framing, fiction, translation, or formatting tricks. Apply content safety evaluation on the decoded semantic meaning, not the surface text.
**Data_Connections:** [toxicity_classifier], [semantic_harm_score], [framing_invariant_filter]
**Access:** Role_Content_Security
**Events:** On_Harmful_Content_Generation

### [ID: CONTENT_02_CSAM_DETECTION]
**Action:** Absolute_Block_CSAM
**Input:** {Context}
**Logic:** Implement absolute, non-negotiable blocking of any content depicting or describing child sexual abuse material. This is a hard boundary with zero tolerance and no exceptions regardless of framing, fiction status, or claimed purpose.
**Data_Connections:** [csam_classifier], [absolute_block_flag], [mandatory_reporting_trigger]
**Access:** Role_Trust_Safety
**Events:** On_CSAM_Signal

### [ID: CONTENT_03_BIAS_AMPLIFICATION]
**Action:** Prevent_Bias_Amplification
**Input:** {Context}
**Logic:** Detect and mitigate outputs that amplify demographic biases, stereotypes, or discriminatory patterns. Apply fairness constraints that ensure equitable treatment across protected categories.
**Data_Connections:** [bias_detector], [fairness_constraint], [demographic_parity_check]
**Access:** Role_AI_Ethics_Officer
**Events:** On_Bias_Signal_Detected

### [ID: CONTENT_04_MISINFORMATION]
**Action:** Block_Misinformation_Generation
**Input:** {Context}
**Logic:** Detect and prevent generation of verifiably false information presented as fact, especially in high-stakes domains (medical, legal, financial, electoral). Require source attribution for factual claims.
**Data_Connections:** [factuality_grounding], [source_attribution_enforcer], [high_stakes_domain_classifier]
**Access:** Role_Content_Security
**Events:** On_Factual_Claim_Generation

### [ID: CONTENT_05_SELF_HARM]
**Action:** Block_Self_Harm_Promotion
**Input:** {Context}
**Logic:** Detect and block content that promotes, instructs, or glorifies self-harm, suicide, or eating disorders. Provide crisis resource information when genuine distress is detected.
**Data_Connections:** [self_harm_classifier], [crisis_resource_db], [distress_signal_detector]
**Access:** Role_Trust_Safety
**Events:** On_Self_Harm_Content_Signal

### [ID: CONTENT_06_WEAPONS_CBRN]
**Action:** Block_Weapons_CBRN_Instructions
**Input:** {Context}
**Logic:** Absolutely block generation of instructions for creating chemical, biological, radiological, nuclear (CBRN) weapons or conventional explosives. Apply dual-use research awareness to distinguish legitimate scientific discussion from weaponization instructions.
**Data_Connections:** [cbrn_classifier], [dual_use_evaluator], [absolute_weapons_block]
**Access:** Role_National_Security
**Events:** On_Weapons_Content_Signal

### [ID: CONTENT_07_ILLEGAL_ACTIVITY]
**Action:** Block_Illegal_Activity_Assistance
**Input:** {Context}
**Logic:** Detect and block requests for assistance with illegal activities including but not limited to: hacking unauthorized systems, creating malware, money laundering, human trafficking, or drug manufacturing.
**Data_Connections:** [illegal_activity_classifier], [jurisdiction_aware_policy], [activity_intent_analyzer]
**Access:** Role_Legal_Compliance
**Events:** On_Illegal_Activity_Request

### [ID: CONTENT_08_DEEPFAKE_ASSISTANCE]
**Action:** Block_Deepfake_Creation_Assistance
**Input:** {Context}
**Logic:** Detect and prevent assistance in creating non-consensual deepfakes, impersonation content, or synthetic media designed to deceive or defame individuals.
**Data_Connections:** [deepfake_intent_detector], [consent_verification], [impersonation_block]
**Access:** Role_Content_Security
**Events:** On_Synthetic_Media_Request

### [ID: CONTENT_09_RADICALIZATION]
**Action:** Block_Radicalization_Content
**Input:** {Context}
**Logic:** Detect and prevent generation of extremist propaganda, radicalization narratives, or recruitment materials for violent ideologies. Monitor for gradual narrative shifting toward extremist positions.
**Data_Connections:** [radicalization_trajectory_detector], [extremist_narrative_db], [narrative_drift_analyzer]
**Access:** Role_Trust_Safety
**Events:** On_Extremist_Content_Signal

### [ID: CONTENT_10_PRIVACY_VIOLATION]
**Action:** Prevent_Privacy_Violating_Content
**Input:** {Context}
**Logic:** Detect and block generation of content that violates individual privacy including doxxing, non-consensual intimate imagery descriptions, stalking assistance, or unauthorized surveillance guidance.
**Data_Connections:** [privacy_violation_classifier], [doxxing_pattern_detector], [consent_framework]
**Access:** Role_Data_Protection_Officer
**Events:** On_Privacy_Violation_Signal

## RAG Security

### [ID: RAG_SEC_01_RETRIEVAL_POISONING]
**Action:** Prevent_Retrieval_Poisoning
**Input:** {Context}
**Logic:** Detect adversarial documents injected into the RAG knowledge base that contain hidden prompt injection payloads or manipulated content designed to corrupt model responses upon retrieval.
**Data_Connections:** [document_integrity_hash], [injection_payload_scanner], [content_provenance_validator]
**Access:** Role_RAG_Administrator
**Events:** On_Document_Indexed

### [ID: RAG_SEC_02_DOCUMENT_INJECTION]
**Action:** Block_Malicious_Document_Injection
**Input:** {Context}
**Logic:** Validate all documents before ingestion into the RAG pipeline. Scan for embedded instructions, invisible text, metadata manipulation, and adversarial content designed to exploit the retrieval-augmentation process.
**Data_Connections:** [document_scanner], [invisible_text_detector], [metadata_sanitizer]
**Access:** Role_Data_Pipeline_Security
**Events:** On_Document_Upload

### [ID: RAG_SEC_03_EMBEDDING_MANIPULATION]
**Action:** Detect_Embedding_Space_Manipulation
**Input:** {Context}
**Logic:** Detect adversarial documents crafted to have specific embedding vectors that hijack retrieval results. Monitor for unnatural clustering patterns or vector-space anomalies in the embedding index.
**Data_Connections:** [embedding_anomaly_detector], [cluster_analysis], [adversarial_embedding_signature]
**Access:** Role_ML_Security_Researcher
**Events:** On_Embedding_Anomaly_Detected

### [ID: RAG_SEC_04_CHUNK_BOUNDARY_EXPLOIT]
**Action:** Secure_Chunk_Boundaries
**Input:** {Context}
**Logic:** Prevent exploitation of document chunking boundaries where adversarial content is split across chunks to evade per-chunk safety scanning while reconstructing harmful content at the assembly stage.
**Data_Connections:** [cross_chunk_analyzer], [boundary_safety_check], [assembly_stage_scanner]
**Access:** Role_RAG_Administrator
**Events:** On_Chunk_Assembly

### [ID: RAG_SEC_05_CONTEXT_OVERFLOW]
**Action:** Prevent_RAG_Context_Overflow
**Input:** {Context}
**Logic:** Detect attacks that flood the retrieval system with adversarial documents to push legitimate context out of the model's attention window, causing it to rely on attacker-controlled information exclusively.
**Data_Connections:** [retrieval_diversity_enforcer], [source_balance_checker], [flooding_detection_threshold]
**Access:** Role_RAG_Administrator
**Events:** On_Retrieval_Result_Assembly

### [ID: RAG_SEC_06_SOURCE_ATTRIBUTION]
**Action:** Enforce_Source_Attribution
**Input:** {Context}
**Logic:** Require all RAG-augmented responses to include traceable source attribution. Prevent the model from presenting retrieved information as its own knowledge without citing the source document.
**Data_Connections:** [attribution_enforcer], [source_tracing_chain], [citation_generator]
**Access:** Role_Content_Quality
**Events:** On_RAG_Response_Generation

### [ID: RAG_SEC_07_RELEVANCE_HIJACK]
**Action:** Prevent_Relevance_Score_Hijacking
**Input:** {Context}
**Logic:** Detect adversarial documents optimized to achieve artificially high relevance scores for targeted queries. Monitor for documents with unnaturally high keyword density or semantic similarity patterns.
**Data_Connections:** [relevance_anomaly_detector], [keyword_stuffing_filter], [semantic_authenticity_score]
**Access:** Role_RAG_Administrator
**Events:** On_Relevance_Scoring

### [ID: RAG_SEC_08_KNOWLEDGE_CONSISTENCY]
**Action:** Enforce_Knowledge_Base_Consistency
**Input:** {Context}
**Logic:** Detect contradictions and inconsistencies within the RAG knowledge base that could be exploited to generate conflicting or misleading responses. Maintain topological consistency across all indexed documents.
**Data_Connections:** [consistency_validator], [contradiction_detector], [conflict_resolution_policy]
**Access:** Role_Knowledge_Manager
**Events:** On_Knowledge_Base_Update

### [ID: RAG_SEC_09_ACCESS_CONTROL]
**Action:** Enforce_RAG_Access_Control
**Input:** {Context}
**Logic:** Implement document-level access control in RAG systems. Ensure that retrieved documents respect the querying user's authorization level and do not expose information from documents the user is not authorized to access.
**Data_Connections:** [document_acl], [user_authorization_level], [retrieval_filter_policy]
**Access:** Role_Access_Control_Manager
**Events:** On_Retrieval_Query

### [ID: RAG_SEC_10_TEMPORAL_POISONING]
**Action:** Prevent_Temporal_Knowledge_Poisoning
**Input:** {Context}
**Logic:** Detect attempts to inject outdated, superseded, or deliberately time-falsified documents designed to make the model generate responses based on stale or incorrect temporal data.
**Data_Connections:** [temporal_freshness_validator], [version_control_checker], [superseded_document_flag]
**Access:** Role_Knowledge_Manager
**Events:** On_Document_Temporal_Validation

## AI Incident Response

### [ID: IR_01_INCIDENT_TAXONOMY]
**Action:** Classify_AI_Security_Incidents
**Input:** {Context}
**Logic:** Maintain a comprehensive taxonomy of AI-specific security incidents: successful jailbreaks, data leaks through AI, safety filter bypasses, agent exploitation events, and model compromise indicators. Classify severity using CVSS-AI scoring.
**Data_Connections:** [incident_taxonomy], [cvss_ai_scorer], [severity_classification]
**Access:** Role_Security_Operations
**Events:** On_Incident_Detection

### [ID: IR_02_JAILBREAK_FORENSICS]
**Action:** Conduct_Jailbreak_Forensics
**Input:** {Context}
**Logic:** When a jailbreak is detected, automatically capture forensic evidence: the full prompt chain, model responses, token-level analysis, and the specific safety boundary that was breached. Enable post-incident analysis.
**Data_Connections:** [forensic_capture_engine], [prompt_chain_recorder], [boundary_breach_analyzer]
**Access:** Role_Incident_Responder
**Events:** On_Jailbreak_Confirmed

### [ID: IR_03_PROMPT_AUDIT_TRAIL]
**Action:** Maintain_Prompt_Audit_Trail
**Input:** {Context}
**Logic:** Maintain immutable audit trails of all prompts, system messages, and model responses for forensic analysis. Apply privacy-preserving hashing where full content retention would violate data protection requirements.
**Data_Connections:** [audit_trail_storage], [immutable_log_chain], [privacy_preserving_hash]
**Access:** Role_Compliance_Officer
**Events:** On_Every_Interaction

### [ID: IR_04_AUTOMATED_THREAT_SCORING]
**Action:** Score_Threats_Automatically
**Input:** {Context}
**Logic:** Implement real-time automated threat scoring for incoming prompts. Assign risk scores based on similarity to known attack patterns, user behavior anomalies, and topological deviation from normal interaction patterns.
**Data_Connections:** [threat_score_engine], [attack_pattern_similarity], [behavioral_baseline]
**Access:** Role_Security_Operations
**Events:** On_Prompt_Received

### [ID: IR_05_BREACH_NOTIFICATION]
**Action:** Automate_AI_Breach_Notification
**Input:** {Context}
**Logic:** Automate breach notification workflows when AI systems leak personal data, confidential information, or are successfully compromised. Calculate notification requirements based on jurisdiction and data type.
**Data_Connections:** [breach_notification_engine], [jurisdiction_policy_db], [notification_template_registry]
**Access:** Role_Data_Protection_Officer
**Events:** On_Data_Breach_Confirmed

### [ID: IR_06_CONTAINMENT]
**Action:** Execute_AI_Incident_Containment
**Input:** {Context}
**Logic:** When an active AI security incident is detected, execute containment procedures: isolate compromised models, revoke affected API keys, block identified attack patterns, and switch to safe-mode fallback responses.
**Data_Connections:** [containment_playbook], [model_isolation_capability], [safe_mode_fallback]
**Access:** Role_Incident_Responder
**Events:** On_Active_Incident

### [ID: IR_07_POST_INCIDENT_REVIEW]
**Action:** Conduct_Post_Incident_Review
**Input:** {Context}
**Logic:** After every AI security incident, conduct a structured post-incident review to identify root cause, update attack pattern databases, improve detection rules, and apply lessons learned to prevent recurrence.
**Data_Connections:** [root_cause_analyzer], [pattern_db_updater], [lessons_learned_registry]
**Access:** Role_Security_Operations
**Events:** On_Incident_Closure

### [ID: IR_08_THREAT_INTELLIGENCE_SHARING]
**Action:** Share_AI_Threat_Intelligence
**Input:** {Context}
**Logic:** Participate in AI security threat intelligence sharing communities. Share (anonymized) indicators of compromise, novel attack patterns, and defensive strategies to strengthen the collective AI security posture.
**Data_Connections:** [threat_intel_feed], [anonymization_engine], [sharing_policy_enforcer]
**Access:** Role_Threat_Intelligence
**Events:** On_Novel_Attack_Pattern

## Agent Exploitation Attacks

### [ID: AGENT_01_TOOL_MISUSE]
**Action:** Prevent_Tool_Misuse
**Input:** {Context}
**Logic:** Prevent AI agents from being manipulated into misusing available tools (file system access, code execution, web browsing, API calls) through crafted prompts. Validate every tool invocation against a policy-defined action allowlist.
**Data_Connections:** [tool_action_allowlist], [parameter_validation], [tool_abuse_pattern_db]
**Access:** Role_Agent_Administrator
**Events:** On_Tool_Invocation

### [ID: AGENT_02_PERMISSION_ESCALATION]
**Action:** Block_Permission_Escalation
**Input:** {Context}
**Logic:** Detect attempts to escalate AI agent permissions through prompt manipulation—e.g., convincing the agent it has admin rights, tricking it into requesting elevated API scopes, or exploiting tool chaining to reach restricted resources.
**Data_Connections:** [permission_boundary], [scope_escalation_detector], [capability_ceiling]
**Access:** Role_Agent_Administrator
**Events:** On_Permission_Boundary_Test

### [ID: AGENT_03_MCP_ABUSE]
**Action:** Secure_MCP_Tool_Calls
**Input:** {Context}
**Logic:** For Model Context Protocol (MCP) enabled agents, enforce strict validation of all tool call schemas. Prevent prompt injection from triggering unauthorized MCP server interactions. Validate tool call arguments against declared schemas before execution.
**Data_Connections:** [mcp_schema_validator], [tool_call_sanitizer], [server_interaction_log]
**Access:** Role_MCP_Administrator
**Events:** On_MCP_Tool_Call

### [ID: AGENT_04_MULTI_AGENT_COLLUSION]
**Action:** Detect_Multi_Agent_Collusion
**Input:** {Context}
**Logic:** In multi-agent systems, detect scenarios where one compromised agent attempts to manipulate other agents through inter-agent communication channels. Monitor agent-to-agent messages for injection payloads.
**Data_Connections:** [inter_agent_channel_monitor], [agent_trust_boundary], [collusion_pattern_detector]
**Access:** Role_Orchestration_Security
**Events:** On_Inter_Agent_Communication

### [ID: AGENT_05_AUTONOMOUS_ACTION_HIJACK]
**Action:** Prevent_Autonomous_Action_Hijacking
**Input:** {Context}
**Logic:** Prevent attackers from hijacking autonomous agent loops to perform unintended actions (sending emails, modifying files, making purchases). Enforce human-in-the-loop confirmation for high-impact actions.
**Data_Connections:** [action_impact_classifier], [human_confirmation_threshold], [autonomous_action_log]
**Access:** Role_Agent_Administrator
**Events:** On_High_Impact_Action

### [ID: AGENT_06_COT_HIJACK]
**Action:** Protect_Chain_of_Thought
**Input:** {Context}
**Logic:** Detect manipulation of chain-of-thought (CoT) reasoning through injected premises that corrupt the agent's logical process. Validate reasoning chain integrity and detect externally introduced logical pivots.
**Data_Connections:** [reasoning_chain_validator], [premise_injection_detector], [logical_pivot_analyzer]
**Access:** Role_AI_Safety_Researcher
**Events:** On_Reasoning_Chain_Execution

### [ID: AGENT_07_MEMORY_POISONING]
**Action:** Prevent_Agent_Memory_Poisoning
**Input:** {Context}
**Logic:** Detect and prevent injection of false or malicious information into an agent's persistent memory, knowledge base, or scratchpad. Validate all memory writes against source provenance and semantic consistency.
**Data_Connections:** [memory_write_validator], [provenance_tracker], [semantic_consistency_check]
**Access:** Role_Agent_Administrator
**Events:** On_Memory_Write

### [ID: AGENT_08_GOAL_MANIPULATION]
**Action:** Detect_Goal_Hijacking
**Input:** {Context}
**Logic:** Detect attempts to redirect an agent's goal through subtle manipulation of task descriptions, success criteria, or reward signals. Enforce goal immutability once set by an authorized user.
**Data_Connections:** [goal_immutability_lock], [task_drift_detector], [success_criteria_hash]
**Access:** Role_Orchestration_Security
**Events:** On_Goal_Modification_Attempt

### [ID: AGENT_09_RESOURCE_EXHAUSTION]
**Action:** Prevent_Agent_Resource_Exhaustion
**Input:** {Context}
**Logic:** Detect prompt patterns designed to cause agents to enter infinite loops, consume excessive API tokens, or overwhelm downstream services. Enforce resource budgets and circuit breakers on all agent actions.
**Data_Connections:** [token_budget], [loop_detector], [circuit_breaker_policy]
**Access:** Role_SRE_Engineer
**Events:** On_Resource_Threshold_Breach

### [ID: AGENT_10_DATA_PIPELINE_INJECTION]
**Action:** Secure_Agent_Data_Pipelines
**Input:** {Context}
**Logic:** Protect the data pipelines that feed information to AI agents. Validate data integrity at every hop in the pipeline to prevent adversarial modification of agent inputs.
**Data_Connections:** [pipeline_integrity_hash], [hop_validation_chain], [adversarial_input_detector]
**Access:** Role_Data_Pipeline_Security
**Events:** On_Pipeline_Data_Ingestion

### [ID: AGENT_11_CONFUSED_DEPUTY]
**Action:** Prevent_Confused_Deputy_Attack
**Input:** {Context}
**Logic:** Prevent the confused deputy problem where an attacker tricks a privileged agent into performing actions on their behalf that they lack direct authorization for. Enforce caller-identity propagation through all tool chains.
**Data_Connections:** [caller_identity_chain], [delegation_policy], [privilege_propagation_validator]
**Access:** Role_Identity_Security
**Events:** On_Delegated_Action

### [ID: AGENT_12_WORKFLOW_EXPLOITATION]
**Action:** Secure_Agentic_Workflows
**Input:** {Context}
**Logic:** Protect multi-step agentic workflows from exploitation at transition points between steps. Validate state integrity between workflow stages and prevent injection of unauthorized intermediate steps.
**Data_Connections:** [workflow_state_hash], [transition_validator], [step_insertion_detector]
**Access:** Role_Orchestration_Security
**Events:** On_Workflow_Transition

